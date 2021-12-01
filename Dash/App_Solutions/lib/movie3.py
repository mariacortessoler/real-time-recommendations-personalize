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
# Components for Movie 3
#############################

MoviePic=html.Div(
            children=[
                html.Img(
                    src=app.get_asset_url("badCountry.jpg"),
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
        dbc.Button("Submit", id="movie-3-button"),
        dbc.Spinner(html.Div(id="movie-3-output")),
    ]
)

    
##############################
#Movie 3 Layout
##############################   

map=html.Div([   
    html.Hr(className='text-muted'),
    
    dbc.Row([
        html.Div([
        html.H3('Bad Country', className="ml-5 mt-2 mb-3")
        ])
      ]),
        
    dbc.Row([
        dbc.Col(
            MoviePic),
        dbc.Col(
            html.Div([
            html.H5('Movie: Bad Country', className="ml-1 mt-4 mb-3"),
            html.Div("In 1983, a veteran Baton Rouge detective, Bud Carter (Willem Dafoe), infiltrates the most powerful criminal enterprise in the South. After taking down it’s top lieutenant and contract killer, Jesse Weiland (Matt Dillon), the detective convinces him to become an informant. Jesse sets out to help bring down the entire organization, including its architect, Lutin (Tom Berenger).")
            ])
               ),    
        
        dbc.Col(
            html.Div([
            html.H5('Write an opinion about this video', className="ml-1 mt-6 mb-3"),
            html.Br(),
            html.Div('Rate this video', className="ml-1 mt-6 mb-3"),
            dcc.Slider(min=1, max=5, marks={i: '{}'.format(i) for i in [1,2,3,4,5]}, value=4, id='movie-3-slider'),
            html.Div('Share your thoughts and opinion with us', className="ml-1 mt-6 mb-3"),
            input_groups,
            loading_spinner
            ])
            )   
        ]),
    ],className="body")
        
        
        
    