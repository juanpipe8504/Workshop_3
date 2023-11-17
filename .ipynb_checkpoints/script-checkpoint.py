from kafka import KafkaProducer, KafkaConsumer
#from confluent_kafka import Producer
from json import dumps, loads
import pandas as pd
import joblib
import psycopg2

config = {
    "user": "postgres",
    "password": "admin",
    "database": "etl_db"
}

def create_connection():
    try:
        cnx = psycopg2.connect(
            host='localhost',
            user=config["user"],
            password=config["password"],
            database=config["database"]
        )
        print('Conexión exitosa!!')
    except psycopg2.Error as e:
        cnx = None
        print('No se puede conectar:', e)
    return cnx

# Función para iterar sobre un DataFrame y enviar columnas a Kafka
def send_dataframe_to_kafka(dataframe, topic):
    producer = KafkaProducer(
        value_serializer=lambda m: dumps(m).encode('utf-8'),
        bootstrap_servers=['localhost:9092'],
    )

    for index, row in dataframe.iterrows():
        # Convertir la fila a un diccionario para enviarla
        row_dict = row.to_dict()
        producer.send(topic, value=row_dict)
        print(f"Row {index} sent to Kafka topic '{topic}'")


def kafka_consumer():
    consumer = KafkaConsumer(
        'kafka_prueba',
        enable_auto_commit=True,
        group_id='my-group-1',
        value_deserializer=lambda m: loads(m.decode('utf-8')),
        bootstrap_servers=['localhost:9092']
        )

    for m in consumer:
        datos = pd.json_normalize(data=m.value)
        modelo_file = "model.pkl"
        model = joblib.load(modelo_file)
        
        datos['prediccion'] = model.predict(datos[['GDP','Family','Life Expectancy','Freedom','Corruption','Generosity']])

        insert_query = """
    INSERT INTO modelo (country, Happiness_Score, GDP, Family, Life_Expectancy, Freedom, Corruption, Generosity, prediccion)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    
        cnx = create_connection()
        cur = cnx.cursor()
        datos_values = datos.values.tolist()
    
        cur.executemany(insert_query, datos_values)
        cur.close()
        cnx.commit()







        
# Carga del modelo
        #modelo_file = "model.pkl"
        #model = joblib.load(modelo_file)