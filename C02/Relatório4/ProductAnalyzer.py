from database import Database
from helper.writeAJson import writeAJson
from dataset.datasetMercado import dataset

db = Database(database="mercado", collection="compras")
db.resetDatabase()

# 1- Total de itens vendidos por dia:
result = db.collection.aggregate([
    {"$unwind": "$produtos"},
    {"$group": {"_id": {"data": "$data_compra"}, "total": {"$sum": "$produtos.quantidade"}}},
    {"$sort": {"_id.data": 1, "total": -1}},
])

writeAJson(result, "1- Total de itens vendidos por dia")

# 2- Produto mais vendido em todas as compras:
result = db.collection.aggregate([
    {"$unwind": "$produtos"},
    {"$group": {"_id": "$produtos.descricao", "total": {"$sum": "$produtos.quantidade"}}},
    {"$sort": {"total": -1}},
])

writeAJson(result, "2- Produto mais vendido em todas as compras")

# 3- Cliente que mais gastou em uma única compra:
result = db.collection.aggregate([
    {"$unwind": "$produtos"},
    {"$group": {"_id": "$cliente_id", "total_gasto": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}}},
    {"$sort": {"total_gasto": -1}},
    {"$limit": 1}
])

writeAJson(result, "3- Cliente que mais gastou em uma única compra")

# 4- Produtos que tiveram uma quantidade vendida acima de 1 unidade:
result = db.collection.aggregate([
    {"$unwind": "$produtos"},
    {"$group": {"_id": "$produtos.descricao", "quantidade_total": {"$sum": "$produtos.quantidade"}}},
    {"$match": {"quantidade_total": {"$gt": 1}}},
    {"$sort": {"quantidade_total": -1}},
])

writeAJson(result, "4- Produtos que tiveram uma quantidade vendida acima de 1 unidade")
