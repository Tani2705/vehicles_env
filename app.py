import pandas as pd
import plotly.express as px
import streamlit as st

# Cargar los datos
car_data = pd.read_csv('vehicles_us.csv.csv')

# Encabezado de la aplicación
st.header('Análisis de anuncios de vehículos en venta')

# Botón para mostrar un histograma
if st.button('Mostrar histograma del odómetro'):
    st.write('Histograma: Distribución del odómetro de los vehículos')
    fig = px.histogram(car_data, x='odometer')
    st.plotly_chart(fig, use_container_width=True)

# Botón para mostrar gráfico de dispersión
if st.button('Mostrar gráfico de dispersión precio vs año'):
    st.write('Gráfico de dispersión: Precio en función del año del vehículo')
    fig2 = px.scatter(car_data, x='model_year', y='price', color='type')
    st.plotly_chart(fig2, use_container_width=True)

