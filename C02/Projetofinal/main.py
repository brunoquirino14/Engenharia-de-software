from database import Database
from crewModel import CrewModel, MemberModel
from cli import CrewsCLI, MembersCLI

# Conectar ao banco de dados
db = Database(database="MonkeyDBLuffy", collection="onepiece")

# Criar modelos
crew_model = CrewModel(database=db)
member_model = MemberModel(database=db)

# Criar CLIs
crews_cli = CrewsCLI(crew_model, member_model)
members_cli = MembersCLI(member_model)

# Menu principal
while True:
    print("\nEscolha o que deseja gerenciar:")
    print("1 - Tripulações")
    print("2 - Membros")
    print("3 - Sair")
    option = input("Opção: ").strip()

    if option == "1":
        crews_cli.run()
    elif option == "2":
        members_cli.run()
    elif option == "3":
        print("O programa está se encerrando, mas OnePiece não!! Até o próximo episódio!")
        break
    else:
        print("Opção inválida! Tente novamente.")
