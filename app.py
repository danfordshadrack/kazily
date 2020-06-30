import dash
import dash_table
import pandas as pd

df = pd.read_csv('gigs.csv')

app = dash.Dash(__name__)

server = app.server

app.layout = dash_table.DataTable(
    id='table',
    columns=[{"name": i, "id": i} for i in df.columns],
    style_cell={'textAlign': 'left'},
    style_header={
        'backgroundColor': 'rgb(230, 230, 230)',
        'fontWeight': 'bold',
        'border': '1px solid pink'
    },
    style_data={ 'border': '1px solid blue',
                 'whiteSpace': 'normal',
                 'height': 'auto'
                  },
    data=df.to_dict('records'),
)

if __name__ == '__main__':
    app.run_server(debug=True)
