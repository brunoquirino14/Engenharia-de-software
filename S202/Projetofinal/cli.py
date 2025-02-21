class CrewsCLI:
    def __init__(self, crew_model, member_model):
        self.commands = {}
        self.crew_model = crew_model
        self.member_model = member_model
        self.add_command("criar", self.create_crew)
        self.add_command("ler", self.read_crew)
        self.add_command("atualizar", self.update_crew)
        self.add_command("deletar", self.delete_crew)

    def add_command(self, name, function):
        self.commands[name.lower()] = function  # Normaliza os comandos para letras minúsculas

    def run(self):
        while True:
            print("\nComandos disponíveis:", ", ".join(self.commands.keys()), "ou 'menu' para voltar ao menu principal.")
            command = input("Entre com um comando: ").strip().lower()
            if command == "quit":
                print("Adeus!")
                break
            elif command == "menu":
                print("Voltando ao menu principal...")
                return
            elif command in self.commands:
                self.commands[command]()
            else:
                print("Comando inválido. Tente novamente.")

    def create_crew(self):
        nome = input("Nome da tripulação: ")
        capitao = input("Nome do capitão: ")
        navio = input("Nome do navio: ")
        
        # Criar tripulação
        crew_id = self.crew_model.create_crew(nome, capitao, navio)
        
        if crew_id:
            print(f"Tripulação criada com ID: {crew_id}")  # Exibir apenas aqui no CLI
            
            # Adicionar membros
            while True:
                membro = input("Adicione um membro (nome:função) ou digite 'done': ")
                if membro.lower() == "done":
                    break
                if ":" not in membro:
                    print("Formato inválido. Use 'nome:função'.")
                    continue
                nome_membro, funcao = membro.split(":", 1)
                self.member_model.add_member(nome_membro.strip(), funcao.strip(), crew_id)
            print("Membros adicionados com sucesso!")
        else:
            print("Erro ao criar tripulação.")


    def read_crew(self):
        id = input("ID da tripulação: ")
        crew = self.crew_model.read_crew_by_id(id)  # Busca a tripulação
        if crew:
            print("Tripulação encontrada:")
            print(crew)  # Exibe a tripulação no CLI
        else:
            print("Tripulação não encontrada.")


    def update_crew(self):
        id = input("ID da tripulação: ")
        nome = input("Nome da tripulação: ")
        capitao = input("Nome do capitão: ")
        navio = input("Nome do navio: ")
        self.crew_model.update_crew(id, nome, capitao, navio)

    def delete_crew(self):
        id = input("ID da tripulação: ")
        self.crew_model.delete_crew(id)


class MembersCLI:
    def __init__(self, member_model):
        self.commands = {}
        self.member_model = member_model
        self.add_command("adicionar", self.add_member)
        self.add_command("listar", self.list_members)
        self.add_command("remover", self.remove_member)

    def add_command(self, name, function):
        self.commands[name.lower()] = function

    def run(self):
        while True:
            print("\nComandos disponíveis:", ", ".join(self.commands.keys()), "ou 'menu' para voltar ao menu principal.")
            command = input("Entre com um comando: ").strip().lower()
            if command == "quit":
                print("Adeus!")
                break
            elif command == "menu":
                print("Voltando ao menu principal...")
                return
            elif command in self.commands:
                self.commands[command]()
            else:
                print("Comando inválido. Tente novamente.")

    def add_member(self):
        nome = input("Nome do membro: ")
        funcao = input("Função do membro: ")
        crew_id = input("ID da tripulação: ")

        # Adicionar membro com validação no modelo
        result = self.member_model.add_member(nome, funcao, crew_id)
        if not result:
            print(f"Falha ao adicionar membro. Verifique se a tripulação com ID {crew_id} existe.")


    def list_members(self):
        crew_id = input("ID da tripulação: ")
        members = self.member_model.find_members_by_crew(crew_id)
        if members:
            print("Membros encontrados:")
            for member in members:
                print(f"ID: {member['_id']}, Nome: {member['nome']}, Função: {member['funcao']}")
        else:
            print("Nenhum membro encontrado para essa tripulação.")


    def remove_member(self):
        member_id = input("ID do membro: ")
        self.member_model.remove_member(member_id)
