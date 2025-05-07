# Importar la biblioteca de Streamlit y otras bibliotecas necesarias
import streamlit as st
import pandas as pd
import plotly_express as px

# Leer el conjunto de datos CSV
car_data = pd.read_csv('vehicles_us.csv')

# Crear un encabezado para la aplicación
st.header("Análisis de Venta de Coches")

# Crear un botón para generar un histograma
hist_button = st.button('Construir histograma')
     
if hist_button: # al hacer clic en el botón
         # escribir un mensaje
         st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
         
         # crear un histograma
         fig = px.histogram(car_data, x="odometer", title="Histograma de Odómetro")
     
         # mostrar un gráfico Plotly interactivo
         st.plotly_chart(fig, use_container_width=True)

# Crear un botón para generar un gráfico de dispersión
scatter_button = st.button('Construir gráfico de dispersión')

if scatter_button: # al hacer clic en el botón
         # escribir un mensaje
         st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')
         
         # crear un gráfico de dispersión
         fig = px.scatter(car_data, x="odometer", y="price", title="Gráfico de Dispersión: Odómetro vs Precio")
     
         # mostrar un gráfico Plotly interactivo
         st.plotly_chart(fig, use_container_width=True)
