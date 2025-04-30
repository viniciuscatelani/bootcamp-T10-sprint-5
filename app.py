# Importação das bibliotecas necessárias
import streamlit as st
import plotly.express as px
import pandas as pd

# Leitura do arquivo
vehicles = pd.read_csv('./vehicles.csv')

# Título do dashboard
st.title("Dashboard de Veículos")

# Checkboxes para gerar os gráficos
build_boxplot = st.checkbox(
    'Gerar o gráfico de preços por condição do veículo')
build_histogram = st.checkbox(
    'Gerar o gráfico de veículos anunciados por ano de fabricação')
build_scatterplot = st.checkbox(
    'Gerar o gráfico da relação entre preço e quilometragem')

# Botão para gerar os gráficos
if build_boxplot:

    # Gráfico 1: Boxplot por condição
    fig1 = px.box(vehicles,
                  x='condition',
                  y='price',
                  title='Distribuição de Preços por Condição do Veículo',
                  labels={'condition': 'Condição', 'price': 'Preço (USD)'},
                  color='condition')

    # Exibição do gráfico
    st.plotly_chart(fig1, use_container_width=True)

if build_histogram:
    # Gráfico 2: Histograma por ano
    fig2 = px.histogram(vehicles,
                        x='model_year',
                        nbins=30,
                        title='Distribuição de Carros por Ano de Fabricação',
                        labels={'model_year': 'Ano de Fabricação'},
                        color_discrete_sequence=['indianred'])

    # Exibição do gráfico
    st.plotly_chart(fig2, use_container_width=True)

if build_scatterplot:
    # Gráfico 3: Dispersão odômetro vs preço
    fig3 = px.scatter(vehicles,
                      x='odometer',
                      y='price',
                      color='condition',
                      title='Relação entre Quilometragem e Preço',
                      labels={'odometer': 'Quilometragem',
                              'price': 'Preço (USD)'},
                      hover_data=['model', 'model_year'])

    # Exibição do gráfico
    st.plotly_chart(fig3, use_container_width=True)

else:
    st.info("Clique nas checkboxes acima para gerar os gráficos.")
