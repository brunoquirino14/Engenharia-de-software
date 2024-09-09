class SimpleCLI:
    def __init__(self):
        self.commands = {}

    def add_command(self, name, function):
        self.commands[name] = function

    def run(self):
        while True:
            command = input("Entre com um comando: ")
            if command == "quit":
                print("Adeus!")
                break
            elif command in self.commands:
                self.commands[command]()
            else:
                print("Comando inválido. Tente novamente.")


class BooksCLI(SimpleCLI):
    def __init__(self, book_model):
        super().__init__()
        self.book_model = book_model
        self.add_command("Criar", self.create_book)
        self.add_command("Ler", self.read_book)
        self.add_command("Atualizar", self.update_book)
        self.add_command("Deletar", self.delete_book)

    def create_book(self):
        titulo = input("Coloque o título: ")
        autor = input("Coloque o autor: ")
        ano = input("Coloque o ano: ")
        preco = input("Coloque o preço: ")
        self.book_model.create_book(titulo, autor, ano, preco)

    def read_book(self):
        id = input("Escreva o ID: ")
        book = self.book_model.read_book_by_id(id)
        if book:
            print(f"Titulo: {book['titulo']}")
            print(f"Autor: {book['autor']}")
            print(f"Ano: {book['ano']}")
            print(f"Preço: {book['preco']}")
            

    def update_book(self):
        id = input("Escreva o ID: ")
        name = input("Escreva o titulo: ")
        autor = input("Escreva o autor: ")
        ano = input("Escreva o ano: ")
        preco = input("Escreva o preço: ")
        self.book_model.update_book(id, name, autor, ano, preco)

    def delete_book(self):
        id = input("Escreva o ID: ")
        self.book_model.delete_book(id)
        
    def run(self):
        print("Bem vindo ao BooksCLI!")
        print("Comandos disponíveis: Criar, Ler, Atualizar, Deletar, quit")
        super().run()
        
