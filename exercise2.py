# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd

# initialize Dash app and initialize the static folder
app = dash.Dash(__name__, static_folder='static')
df = pd.read_csv('static/Pokemon.csv')
# set layout of the page
app.layout = html.Div(children=[

    # set the page heading
    html.H1(children='Python L2 Exercise 2'),

    # set the description underneath the heading
    html.Div(children='''
        This scatterplot was created to help me visualize what Pokemon to use with high Special Attack and Speed stats
    '''),

    # append the visualization to the page
    dcc.Graph(
        id='example-graph',
        figure={
            # configure the data
            'data': [
                # This is how we define a scatter plot. Note that it also uses "go.Scatter",
                # but with the mode to be only "markers"
                go.Scatter(
                    x=df['Sp. Atk'],
                    y=df['Speed'],
                    mode='markers',
                    text=df['Name'],# This line sets the vehicle name as the points' labels.
                    marker={
                        'size': 8,
                        'opacity': .6,  # By making the points a bit transparent, it can alleviate the occlusion issue
                        'color': 'green'
                    }
                )
            ],
            'layout': {
                'title': 'Pokemon Special Attack Points vs. Speed Points',
                # It is always a good practice to have axis labels.
                # This is especially important in this case as the numbers are not trivial
                'xaxis': {'title': 'Sp. Attack Points'},
                'yaxis': {'title': 'Speed Points'},
            }
        }
    )

])

if __name__ == '__main__':
    app.run_server(debug=True)