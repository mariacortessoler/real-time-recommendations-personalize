#############################
# Load the needed libraries
#############################
import pathlib
import dash
from dash.dependencies import Input
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc 
#Recall app
from app import app

###########################################################
# PARAMETERS YOU NEED TO REPLACE
###########################################################
USER_ID='<YOUR_USER_ID>'
EMAIL_ADDRESS='<YOUR_EMAIL>'


#############################
# Links for all the subsections
#############################

nav = dbc.Nav(
    [
        dbc.NavLink("Home", active=True, href="https://www.amazon.com/gp/video/storefront/ref=topnav_storetab_atv?node=2858778011"),
        dbc.NavLink("Store", href="https://www.amazon.com/gp/video/storefront/ref=nav_shopall_aiv_vid?filterId=OFFER_FILTER%3DTVOD"),
        dbc.NavLink("Categories", href="https://www.amazon.com/gp/video/storefront/ref=atv_cat_cs?contentType=merch&contentId=comingtoprime"),
        dbc.NavLink("Customer Service", href="https://www.amazon.com/gp/video/storefront/ref=atv_cat_cs?contentType=merch&contentId=comingtoprime"),
        dbc.NavLink("Gift Cards", href="https://www.amazon.com/gift-cards/b/?ie=UTF8&node=2238192011&ref_=nav_cs_gc"),
        dbc.NavLink("Help", href="https://affiliate-program.amazon.com/help/stripe.html"),
    ]
)

##Title:
title=html.Div([     
      dbc.Row([
          dbc.Col(
              nav, width=6
          ),
          dbc.Col(
              html.Div([html.I(className="fa fa-user fa-2x",  style={'color':'white'})]), width='auto'
          ),
          dbc.Col(
              html.Div(children=[
                  html.H6('Welcome {} !'.format(EMAIL_ADDRESS), className="mr-3 mt-6 mb-3 text-white"),
                  html.H6('Your user ID: {}'.format(USER_ID), className="mr-3 mt-6 mb-3 text-white")]),
              width='auto'
              )         
        ])
],
className="title")


