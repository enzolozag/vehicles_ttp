# Importación de librerías necesarias
import pandas as pd
import plotly.express as px
import streamlit as st

# Leyendo el DataFrame
vehicle_data = pd.read_csv('vehicles_us.csv')

# --------- Corrección y enriquecimiento de datos ---------

# Cambiando el formato de 'date_posted' de texto a datetime
vehicle_data['date_posted'] = pd.to_datetime(vehicle_data['date_posted'], format='%Y-%m-%d')

# Reemplazando valores 1 en 'is_4wd' por 'Yes' y completando valores faltantes con 'No'
vehicle_data['is_4wd'] = vehicle_data['is_4wd'].replace(1, 'Yes').fillna('No')

# Cambiando el tipo de datos de 'cylinders' de numérico a texto (objeto)
vehicle_data['cylinders'] = vehicle_data['cylinders'].astype('object')

# Extrayendo la marca de la columna 'model' y creando una nueva columna 'manufacturer'
vehicle_data['manufacturer'] = vehicle_data['model'].str.split(n=1).str[0]

# --------- Configuración de la página ---------

# Configurando el layout de la página en Streamlit
st.set_page_config(
    layout='wide',                 # Distribución amplia
    page_title='Vehicle Ads Report', # Título de la página
    page_icon='🚘'                 # Icono de la página
)

# Agregando el título principal de la aplicación
st.title('Vehicle Ads :blue[Analysis Report]')

# Botón para mostrar el DataFrame completo
if st.button('Show data'):
    st.write(vehicle_data)


st.header('Select the graphics you want to visualize :eyes:',divider='blue')

# --------- Sección de histograma ---------

# Casilla de verificación para activar la creación del histograma
hist_button = st.checkbox('Create a :green-background[histogram]?')

if hist_button:
    # Título y descripción de la sección de histograma
    st.subheader('Histogram', divider='green')
    st.markdown('An Histogram shows the **distribution of a dataset by displaying the frequencies** (counts) of data points within certain intervals or bins.')

    # Opciones para el histograma
    hist_option1 = st.selectbox(
        'Select a variable for X axis:', 
        ('price', 'model_year', 'odometer', 'days_listed')
    )
    hist_option2 = st.selectbox(
        'Select a descriptive variable:', 
        ('condition', 'transmission', 'fuel', 'is_4wd')
    )
    
    # Opción para normalizar el histograma
    hist_normalize = st.checkbox('Normalize histogram?')

    # Creación del histograma

    fig = px.histogram(
        vehicle_data,
        x=hist_option1,
        color=hist_option2,
        histnorm='probability' if hist_normalize else None
        )
    st.plotly_chart(fig, use_container_width=True)
else:
    st.write('')

# --------- Sección de gráfica de dispersión ---------

# Casilla de verificación para activar la creación de la gráfica de dispersión
scatter_button = st.checkbox('Create a :orange-background[scatter plot]?')

if scatter_button:
    # Título y descripción de la sección de gráfica de dispersión
    st.subheader('Scatter', divider='orange')
    st.markdown('A Scatter Graph shows the **relation between two variables**. Each data point represents the values of two variables, one variable plotted along the x-axis and the other plotted along the y-axis.')

    # Opciones para la gráfica de dispersión
    scatter_option1 = st.selectbox(
        'Select your variable for X axis:', 
        ('price', 'model_year', 'odometer')
    )
    scatter_option2 = st.selectbox(
        'Select your variable for Y axis:', 
        ('odometer', 'model_year', 'price')
    )

    # Creación de la gráfica de dispersión
    fig = px.scatter(vehicle_data, x=scatter_option1, y=scatter_option2)
    st.plotly_chart(fig, use_container_width=True)
else:
    st.write('')

# --------- Sección de gráfica de barras ---------

# Casilla de verificación para activar la creación de la gráfica de barras
bar_button = st.checkbox('Create a :violet-background[bar chart]?')

if bar_button:
    # Título y descripción de la sección de gráfica de barras
    st.subheader('Bar chart', divider='violet')
    st.markdown('A Bar Chart shows categorical data with rectangular bars. Each bar’s height represents the **value for each category**.')

    # Opciones para la gráfica de barras
    bar_option2 = st.selectbox('Select a variable for X axis:', ('manufacturer', 'cylinders', 'fuel', 'is_4wd', 'type'))
    bar_option3 = st.selectbox('Select a variable for legend:', ('type', 'is_4wd', 'fuel', 'cylinders', 'manufacturer'))

    # Creación de la gráfica de barras
    fig = px.bar(
        vehicle_data,
        x=bar_option2,
        y='price',
        color=bar_option3
    )
    st.plotly_chart(fig, use_container_width=True)

