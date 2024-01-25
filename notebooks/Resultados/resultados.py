import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd


df_votacao_candidato_munzona = pd.read_csv('/Users/willianribeiro/Documents/GitHub/analise_exploratoria_dados_tse/data/Resultados/2020/votacao_candidato_munzona_2020/votacao_candidato_munzona_2020_BRASIL.csv', sep=';', encoding='Latin 1')
df_votacao_partido_munzona = pd.read_csv('/Users/willianribeiro/Documents/GitHub/analise_exploratoria_dados_tse/data/Resultados/2020/votacao_partido_munzona_2020/votacao_partido_munzona_2020_BRASIL.csv', sep=';', encoding='Latin 1')

# Supondo que 'df' é seu DataFrame com os dados eleitorais
# df = pd.read_csv('seu_arquivo_de_dados.csv')


cidade = 'UBATUBA'

cargo = 'Vereador'

df_cidade_filtrado_candidato = df_votacao_candidato_munzona[df_votacao_candidato_munzona['NM_MUNICIPIO'] == cidade]

df_cidade_filtrado_cargo_candidato = df_cidade_filtrado_candidato[df_cidade_filtrado_candidato['DS_CARGO'] == cargo]

df_cidade_filtrado_partido = df_votacao_candidato_munzona[df_votacao_candidato_munzona['NM_MUNICIPIO'] == cidade]

df_cidade_filtrado_cargo_partido = df_cidade_filtrado_partido[df_cidade_filtrado_partido['DS_CARGO'] == cargo]

# Criar gráficos com Plotly
grafico_barras = px.bar(df_cidade_filtrado_cargo_candidato, x='NM_CANDIDATO', y='QT_VOTOS_NOMINAIS_VALIDOS')
grafico_pizza = px.pie(df_cidade_filtrado_cargo_partido, names='NM_PARTIDO', values='QT_VOTOS_NOMINAIS_VALIDOS')

# Iniciar app Dash
app = dash.Dash(__name__)

# Definir layout do Dash
app.layout = html.Div([
    html.H1("Dashboard Eleitoral"),
    dcc.Graph(figure=grafico_barras),
    dcc.Graph(figure=grafico_pizza),
    # Adicione aqui os cards das métricas
])

# Rodar o app
if __name__ == '__main__':
    app.run_server(debug=True)
