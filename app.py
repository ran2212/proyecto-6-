import pandas as pd
import plotly.express as px
import streamlit as st

# Título de la aplicación
st.title("Análisis de Vehículos en Venta")

# Leer el conjunto de datos
car_data = pd.read_csv('vehicles_us.csv')

# Crear un botón en la interfaz de usuario
hist_button = st.button('Construir Histograma') 

# Lógica para manejar la acción del botón
if hist_button:  
    # Mensaje que se muestra cuando se hace clic en el botón
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    
    # Crear un histograma usando Plotly Express
    fig_hist = px.histogram(car_data, x="odometer", title="Histograma de Kilometraje")  
    st.plotly_chart(fig_hist, use_container_width=True)

# Crear un gráfico de dispersión
scatter_button = st.button("Construir Gráfico de Dispersión")

# Lógica para el gráfico de dispersión
if scatter_button:
    st.write("Creación de un gráfico de dispersión de precio vs kilometraje")
    
    # Crear un scatter plot usando Plotly Express
    fig_scatter = px.scatter(car_data, x="odometer", y="price", title="Kilometraje vs Precio", color="condition")
    st.plotly_chart(fig_scatter, use_container_width=True)
