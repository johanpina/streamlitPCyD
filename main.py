import streamlit as st

st.title('Hello World')
st.write("Hola mundo este es un texto de prueba")
st.markdown("## Este es un subtitulo")

"""
### Este es una cosa
"""

variable = st.text_input("Escribe algo")
radio = st.radio("Selecciona una opción", ["Opción 1", "Opción 2", "Opción 3"])
st.selectbox("este es mi selector",options=["Edad", "Nombre", "Apellido"])
st.markdown("---")
print(radio)

archivo = st.file_uploader("Sube un archivo",type=["csv","txt","xlsx"])
import pandas as pd

@st.cache_resource
def leer_archivo(archivo):
    if archivo:
        data = pd.read_excel(archivo)
        return data

if archivo:
    data = pd.read_excel(archivo)
    data

col1, col2, col3 = st.columns(3)

with col1:
    st.write("Esta es la columna 1")

with col2:
    st.write("Esta es la columna 2")

with col3: 
    data


tab1, tab2, tab3 = st.tabs(["Tab 1", "Tab 2", "Tab 3"])

with tab1:
    data
with tab2:
    st.write("Este es el tab 2")
    st.slider("Selecciona un valor", min_value=0, max_value=100)
with tab3:
    productos_unicos = data["product"].value_counts()
    productos_unicos


import plotly.graph_objects as go

# Datos para el gráfico
labels = ['Manzanas', 'Bananas', 'Cerezas', 'Duraznos']
values = [450, 300, 150, 100]

# Crear el gráfico
fig = go.Figure(data=[go.Pie(labels=labels, values=values)])

st.plotly_chart(fig)


st.sidebar.markdown("Esta es la barra lateral")