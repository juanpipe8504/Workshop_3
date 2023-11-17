# Análisis de Felicidad Global (Workshop_3)

Este conjunto de scripts en Python realiza un análisis de datos sobre la felicidad global de los años 2015 a 2019. Asegúrate de seguir estos pasos para una ejecución exitosa:

1. **Ejecutar `codigo.py`**: Antes de proceder, ejecuta el archivo `codigo.py` para cargar y procesar los datos de felicidad de los años 2015 a 2019. Este script realiza funciones esenciales, como la carga de datos, la modificación y el procesamiento.

    ```bash
    python codigo.py
    ```

2. **Ejecutar `consumer.py` después de `codigo.py`**: Después de haber ejecutado `codigo.py`, puedes utilizar el script `consumer.py` para realizar acciones adicionales, como la integración con Kafka. Asegúrate de tener las dependencias instaladas antes de ejecutar este script.

    ```bash
    python consumer.py
    ```

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
