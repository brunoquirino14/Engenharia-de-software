from database import Database
from helper.writeAJson import writeAJson

db = Database(database="pokedex", collection="pokemons")
db.resetDatabase()

class pokedex:
    def __init__(self, database: Database):
        _database = Database



#Query apenas para o pikachu
pokemons = db.collection.find()

def getPokemonByName(name: str):
    return db.collection.find({"name": name})

pikachu = getPokemonByName("Pikachu")
writeAJson(pikachu, "pikachu")


#Query para pokemons tipo Lutador
def getPokemonsByType(types: list):
    return db.collection.find({"type": {"$in": types}})

types = ["Fighting"]
pokemons = getPokemonsByType(types)

writeAJson(pokemons, "pokemons_by_type_Fighting")


#Query para pokemons tipo Grama
def getPokemonsByType(types: list):
    return db.collection.find({"type": {"$in": types}})

types = ["Grass"]
pokemons = getPokemonsByType(types)

writeAJson(pokemons, "pokemons_by_type_Grass")


#Query para pokemons tipo Gelo
def getPokemonsByType(types: list):
    return db.collection.find({"type": {"$in": types}})

types = ["Ice"]
pokemons = getPokemonsByType(types)

writeAJson(pokemons, "pokemons_by_type_Ice")


#Query para pokemons tipo Fogo
def getPokemonsByType(types: list):
    return db.collection.find({"type": {"$in": types}})

types = ["Fire"]
pokemons = getPokemonsByType(types)

writeAJson(pokemons, "pokemons_by_type_Fire")