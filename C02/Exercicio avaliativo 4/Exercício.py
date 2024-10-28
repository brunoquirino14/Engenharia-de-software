#1

cassandra_session.execute("DROP TABLE IF EXISTS estoque;")
query = ''' 
    CREATE TABLE estoque(
        id int, 
        nome text, 
        carro text, 
        estante int, 
        nivel int,
        quantidade int,
        primary key((carro), estante, nivel, id)
    );
'''
cassandra_session.execute(query)
cassandra_session.execute("TRUNCATE estoque;")


query = """ INSERT INTO estoque(id, nome, carro, estante, nivel, quantidade) VALUES (%s, %s, %s, %s, %s, %s) """
cassandra_session.execute(query, (5, "Pistão", "Mustang", 4, 1, 167))

query = """ INSERT INTO estoque(id, nome, carro, estante, nivel, quantidade) VALUES (%s, %s, %s, %s, %s, %s) """
cassandra_session.execute(query, (4, "Suspensão", "Argo", 1, 1, 3500))

#2
# a)
query = """ SELECT * FROM estoque WHERE nome = 'Pistao' ALLOW FILTERING; """
result = cassandra_session.execute(query).all()

print("Pecas relacionadas ah 'Pistao': ")
if result is not None:
  for r in result:
    print(r)

# b)
query = """ SELECT AVG(quantidade) FROM estoque; """
result = cassandra_session.execute(query).one()

print("Media aritmetica de pecas em estoque: ")
print(result)

# c)
query = """ SELECT COUNT(*) FROM estoque; """
result = cassandra_session.execute(query).one()

print("Quantidade de colunas 'estoque': ")
print(result)

# d)
query = """ SELECT MAX(quantidade) AS maior_quantidade, MIN(quantidade) AS menor_quantidade FROM estoque; """
result = cassandra_session.execute(query).one()

print("Maior e menor quantidade de pecas no estoque: ")
print(result)

# e)
query = """ SELECT nome, carro, quantidade FROM estoque WHERE estante = 3 ALLOW FILTERING; """
result = cassandra_session.execute(query).all()

print("Pecas na estante 3: ")
if result is not None:
  for r in result:
    print(r)

# f)
query = """ SELECT AVG(quantidade) FROM estoque WHERE nivel = 1 ALLOW FILTERING; """
result = cassandra_session.execute(query).one()

print("Media da quantidade de pecas no nivel 1: ")
print(result)

# g)
query = """ SELECT * FROM estoque WHERE estante < 3 AND nivel > 4  ALLOW FILTERING; """
result = cassandra_session.execute(query).all()

print("Pecas nas estantes <3 e >4: ")
if result is not None:
  for r in result:
    print(r)


#3
while(True):
    try:
        carro = str(input("Digite o nome do carro: "))

        result = cassandra_session.execute(f"SELECT nome, estante, quantidade FROM estoque WHERE carro = '{carro}' ALLOW FILTERING;").all()

        if result is not None:
            for r in result:
                print(r)
    except:
       print("Ate a proxima!")
       break
