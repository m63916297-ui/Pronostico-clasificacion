# Pronostico-clasificacion
Cargar y explorar datos: Cargar los tres conjuntos de datos (dataset_demand_acumulate.csv, dataset_alpha_betha.csv, to_predict.csv) en DataFrames de pandas y realizar una exploración inicial para entender su estructura, tipos de datos y contenido.


# 🚀 API de Predicción de Clasificación Alpha/Betha

Este proyecto expone un modelo de machine learning de clasificación a través de una API REST desarrollada con FastAPI. El modelo está diseñado para predecir si un registro pertenece a la clase **'Alpha'** o **'Betha'** basándose en una serie de características de servicio y facturación.

## 📊 Bases de Datos

El proyecto utiliza tres archivos CSV principales, cada uno con un propósito específico:

### `dataset_demand_acumulate.csv`
- **Descripción:** Contiene la información histórica de la demanda acumulada.
- **Periodo:** Los datos abarcan desde **enero de 2017 (2017-01)** hasta **abril de 2022 (2022-04)**.
- **Formato de Fecha:** Año-Mes.

### `dataset_alpha_betha.csv`
- **Descripción:** Este es el conjunto de datos principal utilizado para entrenar el modelo de clasificación.
- **Contenido:** Incluye más de **7,000 registros** con todas las variables involucradas para realizar la clasificación.
- **Objetivo:** La variable objetivo es la clase del registro ('Alpha' o 'Betha').

### `to_predict.csv`
- **Descripción:** Este archivo sirve como ejemplo para la predicción en tiempo real.
- **Contenido:** Cuenta con **3 registros** que tienen toda la información de características completa, **excepto la demanda y la clase**.
- **Uso:** La API utiliza este tipo de datos para, mediante el modelo de clasificación, predecir y completar la clase faltante.

## 🤖 Modelo de Machine Learning

El proyecto utiliza un modelo de **Gradient Boosting** para la tarea de clasificación. Este modelo fue entrenado con el `dataset_alpha_betha.csv` y es capaz de predecir la clase ('Alpha' o 'Betha') para nuevos registros que se le proporcionen a través de la API.

## 🛠️ Instalación y Ejecución con Docker

La forma más sencilla y recomendada de ejecutar esta aplicación en un entorno de desarrollo o productivo es utilizando Docker y Docker Compose.

### Prerrequisitos
- Asegúrate de tener [Docker](https://www.docker.com/get-started/) y [Docker Compose](https://docs.docker.com/compose/install/) instalados en tu máquina.

### Pasos para la ejecución

1.  **Clona el repositorio** (o asegúrate de tener todos los archivos del proyecto en una carpeta):
    ```bash
    git clone <url-del-repositorio>
    cd <nombre-del-directorio>
    ```

2.  **Construye y ejecuta el contenedor:**
    Desde la raíz del proyecto, ejecuta el siguiente comando. Construirá la imagen de Docker y levantará el contenedor de la API.
    ```bash
    docker-compose up --build
    ```
    Verás un mensaje de Uvicorn indicando que la API está corriendo en `http://0.0.0.0:8000`.

3.  **Para detener el contenedor:**
    Abre otra terminal y ejecuta:
    ```bash
    docker-compose down
    ```

## 📁 Estructura del Proyecto

```
api/
├── main.py                # Código principal de la API en FastAPI
├── requirements.txt       # Dependencias de Python
├── trained_model.pkl      # Modelo de clasificación entrenado (Gradient Boosting)
├── scaler.pkl             # Objeto scaler para normalizar datos numéricos
├── Dockerfile             # Receta para construir la imagen de Docker
├── docker-compose.yml     # Archivo para orquestar la ejecución del contenedor
├── dataset_demand_acumulate.csv
├── dataset_alpha_betha.csv
└── to_predict.csv
```

## 🔍 Probar la API

Una vez que la aplicación esté en funcionamiento, puedes probar el modelo de clasificación de manera muy sencilla gracias a la documentación interactiva de FastAPI.

1.  Abre tu navegador web y navega a la siguiente URL:
    **[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)**

2.  Busca el endpoint `POST /predict/`.

3.  Haz clic en él para expandirlo, luego presiona el botón "Try it out".

4.  Edita el cuerpo de la solicitud (Request body) con los datos que deseas probar. Puedes usar un ejemplo similar al del archivo `to_predict.csv`.

5.  Presiona **"Execute"** para enviar la solicitud y ver la predicción del modelo en la respuesta.

---

**Tecnologías Utilizadas:**
- [FastAPI](https://fastapi.tiangolo.com/): Framework web para crear APIs.
- [Uvicorn](https://www.uvicorn.org/): Servidor ASGI de alta velocidad.
- [Pydantic](https://pydantic-docs.helpmanual.io/): Validación de datos mediante tipos.
- [Pandas](https://pandas.pydata.org/): Manipulación y análisis de datos.
- [Scikit-learn](https://scikit-learn.org/): Librería de machine learning.
- [Docker](https://www.docker.com/): Plataforma para contenerizar aplicaciones.
```
