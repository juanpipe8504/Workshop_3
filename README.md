# Workshop_3

Este código en Python realiza un análisis de datos sobre la felicidad global de los años 2015 a 2019. Utiliza la biblioteca pandas para cargar datos desde archivos CSV correspondientes a cada año. Además, implementa funciones de modificación para normalizar y estandarizar las columnas de interés en cada conjunto de datos.

## Funciones de Modificación

El código define funciones específicas para cada año (2015 a 2019) que renombran columnas y eliminan aquellas que no son necesarias para el análisis. Estas funciones proporcionan coherencia en la estructura de los datos y facilitan la combinación posterior.

## Procesamiento de Datos y Modelo de Regresión Lineal

Después de aplicar las modificaciones a los DataFrames de cada año, se concatenan en uno solo llamado `datos_completos`. Se eliminan filas con valores nulos y se realiza una división en conjuntos de entrenamiento y prueba para un modelo de regresión lineal.

## Integración con Kafka

El código identifica las filas del conjunto de prueba en el conjunto original y crea un nuevo DataFrame llamado `datos_completos_test`. Finalmente, utiliza una función `send_dataframe_to_kafka` para enviar este DataFrame a un sistema Kafka para procesamiento adicional.

## Requisitos

Asegúrate de tener instaladas las siguientes bibliotecas de Python antes de ejecutar el código:
```bash
pip install pandas scikit-learn
