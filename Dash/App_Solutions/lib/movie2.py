#############################
# Load the required libraries
#############################

import dash
from dash.dependencies import Input
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc 
#Recall app
from app import app


#############################
# Components for Movie 2
#############################

MoviePic=html.Div(
            children=[
                html.Img(
                    src=app.get_asset_url("skyfall.jpg"),
                    height='80%',
                    width='70%'
                )
            ], style={'textAlign': 'center'}
        )


input_groups = html.Div(
    [
        dbc.InputGroup(
            [
                dbc.InputGroupAddon("Review title", addon_type="prepend"),
                dbc.Textarea(),
            ],
            className="mb-3",
        ),
        dbc.InputGroup(
            [
                dbc.InputGroupAddon("Review body", addon_type="prepend"),
                dbc.Textarea(),
            ],
            className="mb-3",
        ),
    ]
)

loading_spinner = html.Div(
    [
        dbc.Button("Submit", id="movie-2-button"),
        dbc.Spinner(html.Div(id="movie-2-output")),
    ]
)

    
##############################
#Movie 2 Layout
##############################   

map=html.Div([ 
    html.Hr(className='text-muted'),
    
    dbc.Row([
        html.Div([
        html.H3('Skyfall', className="ml-5 mt-2 mb-3")
        ])
      ]),
        
    dbc.Row([
        dbc.Col(
            MoviePic),
        dbc.Col(
            html.Div([
            html.H5('Movie: Skyfall', className="ml-1 mt-4 mb-3"),
            html.Div("Now in HD. Bond's loyalty to M is tested as her past comes back to haunt her. As MI6 comes under attack, 007 must track down and destroy the threat, no matter how personal the cost. SKYFALL 2012 Danjaq, United Artists, CPII. 007 and related James Bond Trademarks, TM Danjaq")
            ])
               ),    
        
        dbc.Col(
            html.Div([
            html.H5('Write an opinion about this video', className="ml-1 mt-6 mb-3"),
            html.Br(),
            html.Div('Share your opinion with other customers', className="ml-1 mt-6 mb-3"),
            html.Br(),
            html.Div('Rate this video', className="ml-1 mt-6 mb-3"),
            dcc.Slider(min=1, max=5, marks={i: '{}'.format(i) for i in [1,2,3,4,5]}, value=4, id='movie-2-slider'),
            html.Div('Share your thoughts and opinion with us', className="ml-1 mt-6 mb-3"),
            input_groups,
            loading_spinner
            ])
            )   
        ]),
    ],className="body")
        
        
        
    