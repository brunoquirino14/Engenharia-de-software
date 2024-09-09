import threading
import time
import random
from pymongo import MongoClient

# Configurações do MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client.bancoiot
collection = db.sensores

# Função para simular a leitura do sensor
def sensor_thread(sensor_name):
    while True:
        sensor_data = collection.find_one({"nomeSensor": sensor_name})
        
        if sensor_data["sensorAlarmado"]:
            print(f"Atenção! Temperatura muito alta! Verificar {sensor_name}!")
            break
        
        temperatura = round(random.uniform(30, 40), 2)
        print(f"{sensor_name} - Temperatura: {temperatura}°C")
        
        if temperatura > 38:
            collection.update_one(
                {"nomeSensor": sensor_name},
                {"$set": {"valorSensor": temperatura, "sensorAlarmado": True}}
            )
        else:
            collection.update_one(
                {"nomeSensor": sensor_name},
                {"$set": {"valorSensor": temperatura}}
            )
        
        time.sleep(random.randint(1, 5))  # Aguarda entre 1 a 5 segundos para a próxima leitura

# Criação dos documentos dos sensores (caso ainda não existam)
sensores = ["Temp1", "Temp2", "Temp3"]
for sensor in sensores:
    if collection.find_one({"nomeSensor": sensor}) is None:
        collection.insert_one({
            "nomeSensor": sensor,
            "valorSensor": 0,
            "unidadeMedida": "C°",
            "sensorAlarmado": False
        })

# Criação das threads para cada sensor
threads = []
for sensor in sensores:
    t = threading.Thread(target=sensor_thread, args=(sensor,))
    t.start()
    threads.append(t)

# Aguarda a finalização de todas as threads
for t in threads:
    t.join()
