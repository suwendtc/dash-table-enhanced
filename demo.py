import sys
import imp

sys.path.insert(0, r"/mnt/c/Users/Super Bruce/Desktop/tornado/dash/test/dash_table_enhanced")
 
import dash 
import dash_table
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
from collections import OrderedDict
import json
  

df = pd.DataFrame(OrderedDict([
    ('climate', ['Sunny', 'Snowy', 'Sunny', 'Rainy']),
    ('temperature', [13, 43, 50, 30]),
    ('city', ['NYC', 'Montreal', 'Miami', 'NYC']),
    ('days in', [[], [], [], []])
]))
 
app = dash.Dash(__name__)

app.layout = html.Div([
     dash_table.DataTable(
        id='table',
        data=df.to_dict('records'),
        columns=[
            {'id': 'climate', 'name': 'climate', 'presentation': 'dropdown'},
            {'id': 'temperature', 'name': 'temperature'},
            {'id': 'city', 'name': 'city', 'presentation': 'dropdown'},
            {'id': 'days in', 'name': 'days in', 'presentation': 'multiDatesPicker'}
        ],

        editable=True,
        dropdown={
            'climate': {
                'options': [
                    {'label': i, 'value': i}
                    for i in df['climate'].unique()
                ]
            },
            'city': {
                 'options': [
                    {'label': i, 'value': i}
                    for i in df['city'].unique()
                ]
            }
        }
    ),
    html.Pre(id="output")
]) 

@app.callback(Output('output', 'children'), [Input('table', 'data')])
def display_output(data):
    return 'You have entered {}'.format(json.dumps(data, indent=2))


if __name__ == '__main__':
    app.run_server(debug=True)
