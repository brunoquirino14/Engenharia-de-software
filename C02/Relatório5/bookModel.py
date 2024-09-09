from pymongo import MongoClient
from bson.objectid import ObjectId

class BookModel:
    def __init__(self, database):
        self.db = database

    def create_book(self, titulo:str, autor:str, ano:int, preco:int):
        try:
            res = self.db.collection.insert_one({"titulo": titulo},{"Autor": autor},{"Ano": ano},{"Preço": preco})
            print(f"Livro foi criado com o seguinte ID: {res.inserted_id}")
            return res.inserted_id
        except Exception as e:
            print(f"Um erro ocorreu na criação do livro: {e}")
            return None

    def read_book_by_id(self, id: str):
        try:
            res = self.db.collection.find_one({"_id": ObjectId(id)})
            print(f"Livro encontrado: {res}")
            return res
        except Exception as e:
            print(f"Um erro ocorreu na leitura do livro: {e}")
            return None

    def update_book(self, id: str, titulo: str):
        try:
            res = self.db.collection.update_one({"_id": ObjectId(id)}, {"$set": {"name": titulo}})
            print(f"Livro atualizado: {res.modified_count} documento modificado")
            return res.modified_count
        except Exception as e:
            print(f"Um erro ocorreu na atualização do livro: {e}")
            return None

    def delete_book(self, id: str):
        try:
            res = self.db.collection.delete_one({"_id": ObjectId(id)})
            print(f"Livro deletado: {res.deleted_count} documento apagado")
            return res.deleted_count
        except Exception as e:
            print(f"Um erro ocorreu na exclusão do livro: {e}")
            return None