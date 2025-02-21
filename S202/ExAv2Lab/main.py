from database import Database
from TeacherCRUD import TeacherCRUD

# cria uma instância da classe Database, passando os dados de conexão com o banco de dados Neo4j
db = Database("bolt://100.26.4.223:7687", "neo4j", "swaps-steels-cruiser")
db.drop_all()

# Criando uma instância da classe FamilyDatabase para interagir com o banco de dados
teacher_db = TeacherCRUD(db)

# criando, lendo e fazendo update
teacher_db.create('Chris Lima', 1956, '189.052.396-66')
print('Informacoes do prof Chris (nome, ano de nascimento e CPF): ')
print(teacher_db.read('Chris Lima'))
teacher_db.update('Chris Lima', '162.052.777-77')

# deletando
# teacher_db.delete('Chris Lima')

# Fechando a conexão
db.close()