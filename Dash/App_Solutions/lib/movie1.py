#############################
# Load the needed libraries
#############################
import dash
from dash.dependencies import Input
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc 
#Recall app
from app import app


#############################
# Principal
#############################
principal=html.Div(
            children=[
                html.Img(
                    src=app.get_asset_url("Option 3.png"),
                    height='90%',
                    width='60%',
                    id="principal-image",
                )
            ], style={'textAlign': 'center'}
        )

#############################
# Components for movie 1
#############################

MoviePic=html.Div(
            children=[
                html.Img(
                    src=app.get_asset_url("catchingfire.jpg"),
                    height='80%',
                    width='70%',
                    id="movie-1-image",
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
        dbc.Button("Submit", id="movie-1-button"),
        dbc.Spinner(html.Div(id="movie-1-output")),
    ]
)

    
##############################
#Full Layout for movie 1
##############################        
map=html.Div([ 
    html.Br(className="ml-5 mt-5 mb-3"),
    html.Br(className="ml-5 mt-5 mb-3"),
    dbc.Row([
        html.H2("Customer reviews", className="ml-5 mt-5 mb-3")
    ]),
    
    dbc.Row([
        principal
    ]),
    
    html.Hr(className='text-muted'),
    
    dbc.Row([
        html.Div([
        html.H3('The Hunger Games: Catching Fire', id='movie-1-text', className="ml-5 mt-2 mb-3")
        ])
      ]),
        
    dbc.Row([
        dbc.Col(
            MoviePic),
        dbc.Col(
            html.Div([
            html.H5('Movie: The Hunger Games: Catching Fire', className="ml-1 mt-4 mb-3"),
            html.Div("Jennifer Lawrence returns in this thrilling sequel to The Hunger Games. Katniss and Peeta embark on a victory tour while President Snow plots a deadly new Hunger Games that could change Panem forever."
               )
            ])
               ),    
        
        dbc.Col(
            html.Div([
            html.H5('Write an opinion about this video', className="ml-1 mt-6 mb-3"),
            html.Br(),
            html.Div('Share your opinion with other customers', className="ml-1 mt-6 mb-3"),
            html.Br(),
            html.Div('Rate this video', className="ml-1 mt-6 mb-3"),
            dcc.Slider(min=1, max=5, marks={i: '{}'.format(i) for i in [1,2,3,4,5]}, value=4, id='movie-1-slider'),
            html.Div('Share your thoughts and opinion with us', className="ml-1 mt-6 mb-3"),
            input_groups,
            loading_spinner
            ])
            )   
        ]),
    ],className="body")
        
        
        
    