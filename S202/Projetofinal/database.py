from pymongo import MongoClient

class Database:
    def __init__(self, database, collection):
        self.connect(database, collection)

    def connect(self, database, collection):
        try:
            connectionString = "localhost:27017"
            self.clusterConnection = MongoClient(connectionString, tlsAllowInvalidCertificates=True)
            self.db = self.clusterConnection[database]
            self.collection = self.db[collection]
            print("Conectado ao banco de dados com sucesso!")
        except Exception as e:
            print(e)

    def resetDatabase(self):
        try:
            self.collection.drop()  # Apagar coleção atual
            dataset = [
                {"_id": 1, "nome": "Piratas do Chapéu de Palha", "capitao": "Monkey D. Luffy", "navio": "Thousand Sunny", "membros": [
                    {"nome": "Roronoa Zoro", "funcao": "Espadachim"},
                    {"nome": "Nami", "funcao": "Navegadora"},
                    {"nome": "Sanji", "funcao": "Cozinheiro"},
                ]},
                {"_id": 2, "nome": "Piratas do Coração", "capitao": "Trafalgar Law", "navio": "Polar Tang", "membros": [
                    {"nome": "Bepo", "funcao": "Imediato"},
                    {"nome": "Shachi", "funcao": "Combatente"},
                    {"nome": "Penguin", "funcao": "Combatente"},
                ]},
            ]
            self.collection.insert_many(dataset)
            print("Banco de dados resetado com sucesso!")
        except Exception as e:
            print(e)
