from pymongo import MongoClient
from bson.objectid import ObjectId

class CrewModel:
    def __init__(self, database):
        self.db = database

    def create_crew(self, nome: str, capitao: str, navio: str):
        try:
            res = self.db.collection.insert_one({
                "nome": nome,
                "capitao": capitao,
                "navio": navio
            })
            return res.inserted_id  # Retorna apenas o ID criado
        except Exception as e:
            print(f"Erro ao criar tripulação: {e}")
            return None


    def read_crew_by_id(self, id: str):
        try:
            res = self.db.collection.find_one({"_id": ObjectId(id)})
            return res  # Retorna apenas os dados, sem mensagens
        except Exception as e:
            print(f"Erro ao buscar tripulação: {e}")
            return None


    def update_crew(self, id: str, nome: str, capitao: str, navio: str):
        try:
            res = self.db.collection.update_one(
                {"_id": ObjectId(id)},
                {"$set": {"nome": nome, "capitao": capitao, "navio": navio}}
            )
            print(f"Tripulação atualizada: {res.modified_count} documento(s) modificado(s)")
            return res.modified_count
        except Exception as e:
            print(f"Erro ao atualizar tripulação: {e}")
            return None

    def delete_crew(self, id: str):
        try:
            res = self.db.collection.delete_one({"_id": ObjectId(id)})
            print(f"Tripulação deletada: {res.deleted_count} documento(s) apagado(s)")
            return res.deleted_count
        except Exception as e:
            print(f"Erro ao deletar tripulação: {e}")
            return None


class MemberModel:
    def __init__(self, database):
        self.db = database

    def add_member(self, nome: str, funcao: str, crew_id: str):
        try:
            # Verificar se a tripulação existe
            crew_exists = self.db.collection.find_one({"_id": ObjectId(crew_id)})
            if not crew_exists:
                print(f"Erro: A tripulação com ID {crew_id} não existe.")
                return None

            # Adicionar membro
            res = self.db.collection.insert_one({
                "nome": nome,
                "funcao": funcao,
                "crew_id": ObjectId(crew_id)
            })
            print(f"Membro adicionado com ID: {res.inserted_id}")
            return res.inserted_id
        except Exception as e:
            print(f"Erro ao adicionar membro: {e}")
            return None


    def find_members_by_crew(self, crew_id: str):
        try:
            members = self.db.collection.find({"crew_id": ObjectId(crew_id)})
            return list(members)  # Retorna apenas a lista de membros
        except Exception as e:
            print(f"Erro ao buscar membros: {e}")
            return []


    def remove_member(self, member_id: str):
        try:
            res = self.db.collection.delete_one({"_id": ObjectId(member_id)})
            print(f"Membro removido: {res.deleted_count} documento(s) apagado(s)")
            return res.deleted_count
        except Exception as e:
            print(f"Erro ao remover membro: {e}")
            return None
