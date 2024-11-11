import streamlit as st
import pandas as pd
from pypmml import Model
import tempfile

# Crear la interfaz de usuario con Streamlit
st.title('Aplicación de Predicción con Modelos PMML')

# Subir archivo PMML
uploaded_model = st.file_uploader("Sube tu modelo PMML", type=["pmml"])

model = None
if uploaded_model is not None:
    # Guardar el archivo PMML temporalmente
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        tmp_file.write(uploaded_model.read())
        model_path = tmp_file.name
    
    # Cargar el modelo PMML
    model = Model.load(model_path)
    st.success("Modelo cargado exitosamente.")

# Subir archivo CSV o XLSX
uploaded_file = st.file_uploader("Sube tu archivo CSV o XLSX", type=["csv", "xlsx"])

if uploaded_file is not None and model is not None:
    # Leer el archivo según su tipo
    if uploaded_file.name.endswith('.csv'):
        data = pd.read_csv(uploaded_file)
    elif uploaded_file.name.endswith('.xlsx'):
        data = pd.read_excel(uploaded_file, engine='openpyxl')
    
    st.write("Datos cargados:")
    st.write(data)

    # Realizar predicciones para todas las filas
    predictions = model.predict(data)
    st.write("Predicciones:")
    st.write(predictions)

# Ejecutar la aplicación con: streamlit run main.py
