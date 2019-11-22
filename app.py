#!/usr/bin/env python3

from datetime import datetime, timedelta
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import plotly.graph_objs as go
from loan import get_loans
from exceptions import InitializationDataNotFound, ThirdPartyApiUnavailable
import sys


try:
    loans = get_loans()
except InitializationDataNotFound:
    print('[ERROR] Validate \'loan.csv\' and \'btcusd.csv\' files are avaialble' +
          ' in \'/data/\' dir. Terminating execution.')
    sys.exit(1)
except ThirdPartyApiUnavailable:
    print('[ERROR] Third party API not responding, try again later. Terminating execution.')
    sys.exit(1)



for cdp in loans:
    print(cdp)

exit(0)


app = dash.Dash()
app.layout = html.Div([
    # Price ticker
    html.H1(id='btc_price', children='BTC: USD.'),
    dcc.Interval(id='update_interval', interval=10000, n_intervals=0),

    # Time frame selection
    html.Div([
        html.Div([
            html.Label(children='Select time frame:')
        ], style={'width': '150px', 'display': 'inline-block', 'vertical-align': 'middle'}),
        html.Div([
            dcc.Dropdown(id='days_dropbox',
                options=[
                    {'label': '90 days', 'value': 90},
                    {'label': '60 days', 'value': 60},
                    {'label': '30 days', 'value': 30}
                ],
                value=60)
        ], style={'width': '150px', 'display': 'inline-block', 'vertical-align': 'top'})
    ], style={'padding-top': '20px'}),

    html.Div([
        dcc.Graph(id='ratio_graph')
    ])
])

@app.callback(Output('btc_price', 'children'),
              [Input('update_interval', 'n_intervals')])
def update_stats(n_intervals):
    global df_cdp

    # TODO: Need to fix below, price functions were separated
    # price = get_price()
    # df_cdp['coll_ratio'] = update_loan_ratios(df_cdp, price)
    # return 'BTC: '+str(price['USD'])+' USD - '+str(price['CAD'])+' CAD'
    return 'BTC: price is wakawaka'

@app.callback(Output('ratio_graph', 'figure'),
              [Input('days_dropbox', 'days')])
def update_graph(n_days):
    global df_btcusd
    global df_cdp
    data = []
    start_date = (datetime.today() - timedelta(days=n_days)).date()

    trace1 = go.Scatter(x=df_btcusd[df_btcusd['Date'] >= start_date],
                        y=df_cdp['coll_ratio'])



if __name__ == '__main__':
    app.run_server()
