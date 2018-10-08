
from bsread import source, PULL
import threading
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go


imgData = None
metaData = {}


def receive_stream():
    """
      Receive stream data through the provided port.
      Store stream in message variable.
      >> metaData['beam'] : Stores Beam_energy value.
      >> metaData['repRate'] : Stores repetition_rate value.
      >> imgData : global variable tha stores generated image.
    """
    with source(host = 'localhost',port=3000, mode = PULL) as stream:

        while True:
            message = stream.receive()
            metaData['beam']= message.data.data['beam_energy'].value
            metaData['repRate'] = message.data.data['repetition_rate'].value

            global imgData
            imgData = message.data.data["image"].value


t1 = threading.Thread(target=receive_stream)
t1.start()

"""
    Create Dash Application called 'app'. 
    Create app layout which includes:
    >> html.div: Creates a html div tag.
    >> html.H2: Creates a html heading 2 tag.
    >> dcc.interval: Updates the Dash app every 5 seconds.

"""
app = dash.Dash(__name__)
app.layout = html.Div(

    html.Div([
        html.H2('RECEIVED STREAMS'),
        html.Div(id='displaying-an-image'),
        html.H2(id = 'metadata'),
        dcc.Interval(
            id='interval-component',
            interval=1 * 5000,  # in milliseconds
            n_intervals=0)
    ])
)


@app.callback(Output('displaying-an-image', 'children'),
              [Input('interval-component', 'n_intervals')])
def display_heatmap(p):
    """
    Creates a Heat map from the imgData Data.
    >> trace: Stores heat map
    >> data: Stores trace as a list
    >> layout: Defines the layout of the heat map
    >> return: Returns 'data' and 'layout' in the figure property of the Dash Graph
    """
    global imgData
    trace = go.Heatmap(z=imgData)
    data = [trace]
    layout = go.Layout(title="HEAT MAPS", xaxis= {'title': 'X axis'}, yaxis={'title': 'Y axis'})

    return dcc.Graph(figure={
                            'data': data,
                            'layout': layout
                            })


@app.callback(Output('metadata', 'children'),
             [Input('interval-component', 'n_intervals')])
def update_metadata(p):
    """
    >> return: Returns metaData value
    """
    for key in metaData:
        return metaData[key]


if __name__ == '__main__':
    app.run_server(debug=True ,port=8080, host=0.0)


