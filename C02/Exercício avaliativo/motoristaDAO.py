from pymongo import MongoClient
from bson.objectid import ObjectId

import Corrida

class MotoristaDAO:
    def __init__(self, database):
        self.db = database

    def create_motora(self, corridas: Corrida, nota: int):
        try:
            # Insere no banco de dados
            res = self.db.collection.insert_one({"Corrida": corridas, "Nota": nota})
            print(f"Motorista criado com o ID: {res.inserted_id}")
            return res.inserted_id
        except Exception as e:
            print(f"Ocorreu um erro ao inserir motorista: {e}")
            return None

    def read_motora_by_id(self, id: str):
        try:
            res = self.db.collection.find_one({"_id": ObjectId(id)})
            if res is None:
                print("Erro: Motorista não encontrado.")
                return None
            return res
        except Exception as e:
            print(f"Ocorreu um erro ao ler o motorista: {e}")
            return None
        
    def update_motora(self, id: str, nota: int, corridas: list):
        try:
            # Converter o id em ObjectId se necessário
            id = ObjectId(id)
            print(f"Tentando atualizar o motorista com ID: {id}")

            # Atualiza o motorista no banco de dados
            res = self.db.collection.update_one(
                {"_id": id},  # Filtra pelo ID do motorista
                {
                    "$set": {
                        "Nota": nota,
                        "Corrida": corridas
                    }
                }
            )
            
            if res.modified_count == 0:
                print("Nenhum motorista encontrado com o ID fornecido ou nenhuma alteração foi necessária.")
            else:
                print(f"Motorista alterado: {res.modified_count} documento(s) modificados.")
            
            return res.modified_count
        except Exception as e:
            print(f"Ocorreu um erro ao alterar o motorista: {e}")
            return None




    def delete_motora(self, id: str):
        try:
            # Converter o id em ObjectId se necessário
            id = ObjectId(id)
            # Exclui o motorista do banco de dados
            res = self.db.collection.delete_one({"_id": id})  # Use _id aqui

            if res.deleted_count > 0:
                print(f"Motorista com ID {id} excluído com sucesso.")
                return True
            else:
                print("Nenhum motorista encontrado com o ID fornecido.")
                return False
        except Exception as e:
            print(f"Ocorreu um erro ao excluir o motorista: {e}")
            return False

