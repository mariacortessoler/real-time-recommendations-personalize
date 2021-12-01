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

####################################################################################
# Add the Amazon Logo image
####################################################################################

Logo_Img=html.Div(
            children=[
                html.Img(
                    src=app.get_asset_url("whiteLogo.png"),
                     height='100%',
                     width='70%',
                    id="logo-image",
                    className='text-center'
                )
            ], style={'textAlign': 'center'}
        )

deals=html.Div(
            children=[
                html.Img(
                    src=app.get_asset_url("memberDeals.jpg"),
                     height='100%',
                     width='100%',
                    id="deals-image"
                )
            ], style={'textAlign': 'center'}
        )


#############################################################################
# Sidebar Layout
#############################################################################
sidebar=html.Div(
    [   Logo_Img, #Add the Amazon Logo image located in the assets folder
        html.Hr(), #Add an horizontal line
        html.H5("It's easy to watch Prime Video on your device.", className='text-white text-center'), #Add an horizontal line
        html.Div("Locate your device, follow the simple instructions and you'll be able to start watching instantly.", className='text-white-50 text-center'),
        html.Br(),
        html.Hr(className='text-muted'),
        ####################################################
        html.H5("Prime Member Deals", className='text-white'),
        deals,
        #Place the rest of Layout here
        ####################################################
        html.Br(),
        html.Hr(className='text-muted'),
        html.H4("RENT OR BUY", className='text-white'),
        html.H5("New release movies", className='text-white'),
        dbc.Row([
            dbc.Col(html.Img(src=app.get_asset_url("deepBlueSea.jpeg"),
                    height='100%',
                    width='100%',
                    id="blue-image")),
            dbc.Col(html.Img(src=app.get_asset_url("mostWanted.jpg"),
                    height='100%',
                    width='100%',
                    id="wanted-image")),
        ]),

        html.Hr()
    ],className='sidebar'
    
)





