import pyodbc
import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html

# data
server = 'ena6obg6j2cevcppw7dn7yu57a-ft5kzcrrso7exn77ioi727kmza.datawarehouse.fabric.microsoft.com'
database = 'cidade_inteligente'

conn = pyodbc.connect(
    f"Driver={{ODBC Driver 18 for SQL Server}};"
    f"Server={server};"
    f"Database={database};"
    "Authentication=ActiveDirectoryInteractive"
)

query = """
SELECT TOP (10) [ano],
            [sigla_uf],
            [id_municipio],
            [quantidade_vinculos_ativos],
            [quantidade_vinculos_clt],
            [quantidade_vinculos_estatutarios],
            [tamanho_estabelecimento],
            [cnae_1]
FROM [cidade_inteligente].[dbo].[rais_estab]
"""

df = pd.read_sql(query, conn)

fig = px.histogram(df, x="quantidade_vinculos_ativos", nbins=20)

app = Dash(__name__)

app.layout = html.Div([
    dcc.Graph(figure=fig)
])

app.run_server(debug=True)
