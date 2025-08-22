import pandas as pd
import plotly.express as px
import streamlit as st
from pathlib import Path

# cabeçalho do app
st.header('Dashboard de vendas de carros')

# carregar dados
car_data = pd.read_csv(Path('data/vehicles.csv'))

# botão para histograma
hist_button = st.button('Criar histograma')
if hist_button:
    st.write('Criando um histograma para odometer')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

# botão para gráfico de dispersão
scatter_button = st.button('Criar gráfico de dispersão')
if scatter_button:
    st.write('Criando um gráfico de dispersão para odometer x price')
    fig2 = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig2, use_container_width=True)
