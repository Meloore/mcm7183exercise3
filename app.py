from dash import Dash, html, dcc
import numpy as np
import pandas as pd
import plotly.express as px


app = Dash(__name__)
server = app.server

app.layout = html.H1('Hello World!')

if __name__ == '__main__':
    app.run(debug=True)
