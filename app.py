import pandas as pd
import plotly.express as px
import streamlit as st

# Leer el conjunto de datos
car_data = pd.read_csv('vehicles_us.csv')

# Crear un botón en la interfaz de usuario
hist_button = st.button('Construir histograma') 

# Lógica para manejar la acción del botón
if hist_button:  
    # Mensaje que se muestra cuando se hace clic en el botón
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    
    # Crear un histograma usando Plotly Express
    fig = px.histogram(car_data, x="odometer")  
    
    # Mostrar el gráfico de Plotly en la aplicación
    st.plotly_chart(fig, use_container_width=True)  
