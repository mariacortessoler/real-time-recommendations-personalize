#############################
# Load the needed libraries
#############################
import pathlib
import dash
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
import dash_core_components as dcc
import dash_html_components as html
#Dash Bootstrap Components
import dash_bootstrap_components as dbc 
#API request 
import json
import requests
#Recall app
from app import app

###########################################################
# PARAMETERS YOU NEED TO REPLACE
###########################################################

INVOKE_URL='<YOUR_API_INVOCATIONS_URL>'
API_KEY='<YOUR_API_KEY>'
USER_ID='<YOUR_USER_ID>' 
EMAIL_ADDRESS='<YOUR_EMAIL>'

###########################################################
# APP LAYOUT:
###########################################################

#LOAD THE DIFFERENT MOVIES
from lib import title, sidebar, movie1, movie2, movie3

#PLACE THE COMPONENTS IN THE LAYOUT
app.layout =html.Div(
    [ 
      movie1.map,
      movie2.map,
      movie3.map,
      title.title,
      sidebar.sidebar,
    ],
    className="amazon-app", #You can also add your own css files by locating them into the assets folder
)

 
    
###############################################   
#           APP INTERACTIVITY:
###############################################


#############################################################
#Movie 1
#############################################################

@app.callback(Output(component_id='movie-1-output', component_property='children'),
              [Input('movie-1-button','n_clicks')],
              [State('movie-1-slider','value')])

def press_button(n_clicks, rating):
    response='None'
    answer="No rating submitted"
    
    if n_clicks!=None:    
        payload={"user_id": USER_ID,
                 "item_id": 'The Hunger Games: Catching Fire',
                 "event_rating": rating,
                 "event_verified_purchase": "Y",
                 "event_type": "RATING",
                 "email_address": EMAIL_ADDRESS}
        response = requests.post(INVOKE_URL, json=payload, headers={'x-api-key': API_KEY})
        
        if response!=None:
            answer="Success!"
        
    return answer

#############################################################
#Movie 2
#############################################################
@app.callback(Output(component_id='movie-2-output', component_property='children'),
              [Input('movie-2-button','n_clicks')],
              [State('movie-2-slider','value')])

def press_button(n_clicks, rating):
    response='None'
    answer="No rating submitted"
    
    if n_clicks!=None:    
        payload={"user_id": USER_ID,
                 "item_id": 'Skyfall',
                 "event_rating": rating,
                 "event_verified_purchase": "Y",
                 "event_type": "RATING",
                 "email_address": EMAIL_ADDRESS}
        response = requests.post(INVOKE_URL, json=payload, headers={'x-api-key': API_KEY})
        
        if response!=None:
            answer="Success!"
        
    return answer


#############################################################
#Movie 3
#############################################################
@app.callback(Output(component_id='movie-3-output', component_property='children'),
              [Input('movie-3-button','n_clicks')],
              [State('movie-3-slider','value')])

def press_button(n_clicks, rating):
    response='None'
    answer="No rating submitted"
    
    if n_clicks!=None:    
        payload={"user_id": USER_ID,
                 "item_id": 'Bad Country',
                 "event_rating": rating,
                 "event_verified_purchase": "Y",
                 "event_type": "RATING",
                 "email_address": EMAIL_ADDRESS}
        response = requests.post(INVOKE_URL, json=payload, headers={'x-api-key': API_KEY})
        
        if response!=None:
            answer="Success!"
        
    return answer

    
if __name__ == "__main__":
    app.run_server(host='0.0.0.0',port='8080', debug=True, use_reloader=False)
