#######################################################
# Main APP definition.
#
# Dash Bootstrap Components used for main theme and better
# organization. 
#######################################################

import dash
import dash_bootstrap_components as dbc 

external_url='https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css'

app = dash.Dash(__name__, external_stylesheets = [dbc.themes.BOOTSTRAP, external_url])
server = app.server

#We need this for function callbacks not present in the app.layout
app.config.suppress_callback_exceptions = True




