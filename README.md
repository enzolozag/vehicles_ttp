# Análisis y Visualización de Datos de Vehículos

## Descripción del Proyecto
Este proyecto proporciona una aplicación web para analizar y visualizar datos de anuncios de vehículos. Los usuarios pueden explorar varios aspectos del conjunto de datos, como tendencias de precios, distribuciones y correlaciones, a través de gráficos interactivos. 

Puedes acceder a la aplicación desplegada [aquí](https://vehicles-ttp.onrender.com/).

## Funcionalidades
* **Histogramas Interactivos**:<br>Visualiza la distribución de datos con opciones para normalización.
* **Gráficos de Dispersión**:<br>Explora relaciones entre dos variables numéricas.
* **Gráficos de Barras**:<br>Compara datos categóricos como fabricantes o tipos de combustible.

## Visualizaciones
1. **Histogramas**<br>
   Visualiza la distribución de datos numéricos. Puedes normalizar el histograma para mostrar proporciones.

2. **Gráficos de Dispersión**<br>
   Explora la relación entre dos variables numéricas.

3. **Gráficos de Barras**<br>
   Compara diferentes categorías, como tipos de vehículos o tipos de combustible.

## Configuración
* **Diseño de la Página**: La aplicación utiliza un diseño ancho para una mejor visualización de los gráficos.
* **Título e Icono de la Página**: Personaliza el título y el icono editando `st.set_page_config` en `app.py`.

## Datos
El conjunto de datos utilizado en este proyecto es `vehicles_us.csv`, que contiene las siguientes columnas:

* **price**: Precio del vehículo.
* **model_year**: Año en que se fabricó el modelo del vehículo.
* **model**: Modelo del vehículo.
* **condition**: Estado del vehículo (e.g., nuevo, usado).
* **cylinders**: Número de cilindros en el motor del vehículo.
* **fuel**: Tipo de combustible que utiliza el vehículo.
* **odometer**: Distancia que ha recorrido el vehículo.
* **transmission**: Tipo de transmisión (e.g., manual, automática).
* **type**: Tipo de vehículo (e.g., sedán, SUV).
* **paint_color**: Color del vehículo.
* **is_4wd**: Indica si el vehículo tiene tracción en las cuatro ruedas.
* **date_posted**: Fecha en que se publicó el anuncio del vehículo.
* **days_listed**: Número de días que el vehículo estuvo listado antes de ser vendido o retirado.

## Estructura del Proyecto

El repositorio contiene los siguientes archivos:

├── .gitignore<br>
├── .streamlit<br>
│   └── config.toml<br>
├── Notebooks<br>
│   └── EDA.ipynb<br>
├── README.md<br>
├── app.py<br>
├── requirements.txt<br>
└── vehicles_us.csv<br>


- `.gitignore`: Lista de archivos y carpetas que Git debe ignorar.
- `.streamlit/config.toml`: Archivo de configuración para Streamlit.
- `Notebooks/EDA.ipynb`: Notebook de Jupyter para Análisis Exploratorio de Datos.
- `README.md`: Archivo de descripción del proyecto.
- `app.py`: Código principal de la aplicación Streamlit.
- `requirements.txt`: Archivo que contiene las dependencias del proyecto.
- `vehicles_us.csv`: Conjunto de datos utilizado en el análisis.

## Uso
1. **Acceso a la Aplicación**: Visita la aplicación en [este enlace](https://vehicles-ttp.onrender.com/).
2. **Instalar Dependencias**: Si deseas ejecutar la aplicación localmente, usa `pip install -r requirements.txt` para instalar todas las dependencias necesarias.
3. **Ejecutar la Aplicación**: Usa el comando `streamlit run app.py` para iniciar la aplicación web localmente.

   

