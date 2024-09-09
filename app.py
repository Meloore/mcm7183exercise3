from dash import Dash, html, dcc, callback, Input, Output
import numpy as np 
import pandas as pd 
import plotly.express as px



app = Dash(__name__)
server = app.server

app.layout = html.H1('Hello World!')

if __name__ == '__main__':
    app.run(debug=True)

df = pd.read_csv("https://raw.githubusercontent.com/wenjiun/MCM7183Exercise3/main/assets/gdp_1960_2020.csv")
subset_Country = df[df['country'].isin(["Malaysia"])]
fig = px.scatter(subset_Country, x="year", y="gdp")

subset_2020 = df[df['year'].isin([2020])]
subset_2020_Asia = subset_2020[subset_2020['state'].isin(["Asia"])]
subset_2020_Africa = subset_2020[subset_2020['state'].isin(["Africa"])]
subset_2020_America = subset_2020[subset_2020['state'].isin(["America"])]
subset_2020_Europe = subset_2020[subset_2020['state'].isin(["Europe"])]
subset_2020_Oceania = subset_2020[subset_2020['state'].isin(["Oceania"])]
pie_data = [sum(subset_2020_Asia['gdp']),sum(subset_2020_Africa['gdp']),sum(subset_2020_America['gdp']),sum(subset_2020_Europe['gdp']),sum(subset_2020_Oceania['gdp'])];
mylabels = ["Asia", "Africa", "America", "Europe","Oceania"]
pie_df = {'Continent': mylabels,'GDP': pie_data}
fig2 = px.pie(pie_df,values="GDP",names="Continent")

return fig, fig2

image_path = 'assets/logo-mmu.png'

app.layout = [html.H1('MCM7183 Exercise 3'), 
              html.Img(src=image_path), 
              dcc.Dropdown(['Malaysia', 'Indonesia', 'China'], 'Malaysia', id='dropdown-country'),
              dcc.Graph(figure=fig), 
              dcc.Graph(figure=fig2)]

@callout ( Output('graph-scatter', 'figure'),
    Output('graph-pie', 'figure'),
    Input('dropdown-country', 'value'),
    Input('dropdown-year', 'value'),
    )

def update_graph(country_selected):
    subset_Country = df[df['country'].isin([country_selected])]
    fig = px.scatter(subset_Country, x="year", y="gdp")
    return fig

if __name__ == '__main__':
    app.run(debug=True)