###################
## AWS_REGION is set in the Lambda function and is set via environment variables
## PROJECT_ID is set in the Lambda function and is set via environment variables
## CAMPAIGN_ARN is set in the Lambda function and is set via environment variables
## TRACKER_NAME is set in the Lambda function and is set via environment variables
## USER_ID is set in the Lambda function and should be passed in as an argument
## ENDPOINT_ID is set to USER_ID so the Personalize dataset user_id recommendations are stored in a corresponding Pinpoint endpoint

import os
from datetime import datetime
import json
import boto3
import logging;
from botocore.exceptions import ClientError
import uuid
import time

aws_region = os.environ.get('REGION')
project_id = os.environ.get('PROJECT_ID')
campaign_arn = os.environ.get('CAMPAIGN_ARN')
tracker_name=os.environ.get('TRACKER_NAME')

personalize           = boto3.client('personalize')
personalize_runtime   = boto3.client('personalize-runtime')
personalize_events    = boto3.client('personalize-events')
pinpoint = boto3.client('pinpoint')

#Receives the data and metadata from the API Gateway trigger
def lambda_handler(event, context):

    user_id,item_id,event_rating, event_verified_purchase, event_type, email_address=event.get('user_id'),event.get('item_id'),event.get('event_rating'),event.get('event_verified_purchase'),event.get('event_type'),event.get('email_address')
    timestamp=time.time()
    endpoint_id = user_id
    session_id=str(uuid.uuid1())
    tracking_id = retrieve_tracking_id(tracker_name)

    send_new_review(user_id, item_id, timestamp, event_rating, event_verified_purchase, event_type, session_id, tracking_id)

    if is_campaign_active(campaign_arn):
        time.sleep(2)
        itemList = get_recommended_items(user_id, campaign_arn)

    response = update_pinpoint_endpoint(project_id,endpoint_id,item_id, itemList, email_address)

    return {
        'statusCode': 200,
        'user_id': user_id,
        'list': response,
        'body': json.dumps('Lambda execution completed.')
    }

def retrieve_tracking_id(tracker_name):
    tracking_id = ''
    resp = personalize.list_event_trackers()
    trackers = resp['eventTrackers']
    for t in trackers:
        if t['name'] == tracker_name:
            event_tracker_arn = t['eventTrackerArn']
            d_resp = personalize.describe_event_tracker(eventTrackerArn = event_tracker_arn)
            tracking_id = d_resp['eventTracker']['trackingId']
    return tracking_id

def is_campaign_active(campaign_arn):
    _is_active = False

    try:
        _resp = personalize.describe_campaign(campaignArn = campaign_arn)
        _campaign_status = _resp['campaign']['status']
        if _campaign_status == 'ACTIVE':
            _is_active = True
    except Exception as e:
        pass

    return _is_active

# Simulates a review to send an event to Amazon Personalize
def send_new_review(user_id, item_id, timestamp, event_rating, event_verified_purchase, event_type, session_id, tracking_id):

    # Configure Properties:
    event = {
        'itemId': str(item_id),
        'eventRating': event_rating,
        'eventVerifiedPurchase': event_verified_purchase
    }
    event_json = json.dumps(event)

    # Make Call
    personalize_events.put_events(
        trackingId = tracking_id,
        userId     = str(user_id),
        sessionId  = session_id,
        eventList  = [{
            'sentAt': timestamp,
            'eventType': event_type,
            'properties': event_json
            }]
    )


def get_recommended_items(user_id, campaign_arn):
    response = personalize_runtime.get_recommendations(campaignArn=campaign_arn,
                                                       userId=str(user_id),
                                                       numResults=5)
    itemList = response['itemList']
    return itemList

def update_pinpoint_endpoint(project_id,endpoint_id, item_id, itemList, email_address):
    itemlistStr = []

    for item in itemList:
        itemlistStr.append(item['itemId'][0:100])

    pinpoint.update_endpoint(
        ApplicationId=project_id,
        EndpointId=endpoint_id,
        EndpointRequest={
            'Address': email_address,
            'ChannelType':'EMAIL',
            'EndpointStatus': 'ACTIVE',
            'User': {
                'UserAttributes': {
                    'recommended_items':
                        itemlistStr
                                },
                'UserId': endpoint_id
                            }
                        }
        )

    pinpoint.send_users_messages(
    ApplicationId=project_id,
    SendUsersMessageRequest={
        'MessageConfiguration':{'EmailMessage': {'FromAddress': 'Prime Video <xxxx@xxxx.com>'}},
        'TemplateConfiguration': {'EmailTemplate': {'Name': 'personalized-recommendations'}},
        'Users': {endpoint_id:{'Substitutions': {'User.UserAttributes.recommended_items': itemlistStr}}}
    }
    )


    return itemlistStr
