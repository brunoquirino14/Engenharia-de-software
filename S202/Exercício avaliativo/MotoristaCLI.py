from numpy import quantile
import Corrida
import Passageiro
import Motorista


class SimpleCLI:
    def __init__(self):
        self.commands = {}

    def add_command(self, name, function):
        self.commands[name] = function

    def run(self):
        while True:
            command = input("Entre com o comando: ")
            if command == "Sair":
                print("Tchau, brigado!")
                break
            elif command in self.commands:
                self.commands[command]()
            else:
                print("Comando inválido. Tente novamente.")


class motoraCLI(SimpleCLI):
    def __init__(self, motora_model):
        super().__init__()
        self.motora_model = motora_model
        self.add_command("Inserir", self.create_motora)
        self.add_command("Ler", self.read_motora)
        self.add_command("Alterar", self.update_motora)
        self.add_command("Excluir", self.delete_motora)

    def create_motora(self):
        try:
            corridas = []  # Lista para armazenar as corridas
            while True:
                # Solicita os dados da corrida
                nota_corrida = int(input("Nota da corrida: "))
                distancia = float(input("Distância da corrida (em km): "))
                valor = float(input("Valor da corrida (em reais): "))
                
                # Solicita os dados do passageiro
                nome_passageiro = input("Nome do passageiro: ")
                documento_passageiro = input("Documento do passageiro: ")

                # Cria o objeto Passageiro
                passageiro = Passageiro.Passageiro(nome=nome_passageiro, documento=documento_passageiro)

                # Cria o objeto Corrida
                corrida = Corrida.Corrida(nota=nota_corrida, distancia=distancia, valor=valor, passageiro=passageiro)
                corridas.append(corrida.to_dict())  # Adiciona a corrida à lista
                
                # Pergunta se deseja adicionar mais corridas
                adicionar_mais = input("Deseja adicionar outra corrida? (s/n): ")
                if adicionar_mais.lower() != 's':
                    break

            # Solicita a nota geral do motorista
            nota_motorista = int(input("Insira a nota do motorista: "))

            # Cria o motorista no modelo, inserindo todas as corridas
            self.motora_model.create_motora(corridas, nota_motorista)
            print("Motorista e corridas inseridos com sucesso!")
        
        except ValueError:
            print("Erro: Certifique-se de inserir números válidos para nota, distância e valor.")
        except Exception as e:
            print(f"Erro ao criar motorista: {e}")

    def read_motora(self):
        id = input("Entre com o ID do motorista: ")
        motora = self.motora_model.read_motora_by_id(id)

        if motora:
            print("Motorista encontrado:")  # Adiciona depuração
            # Acesse as corridas diretamente
            corridas = motora.get('Corrida', [])  # A chave aqui é 'Corrida'
            if corridas:
                for i, corrida in enumerate(corridas, start=1):
                    print(f"\nCorrida {i}:")
                    print(f"  Nota: {corrida['nota']}")
                    print(f"  Distância: {corrida['distancia']} km")
                    print(f"  Valor: R${corrida['valor']:.2f}")
                    print(f"  Passageiro: {corrida['passageiro']['nome']} (Documento: {corrida['passageiro']['documento']})")
            else:
                print("Nenhuma corrida encontrada.")
        else:
            print("Motorista não encontrado.")


                        


    def update_motora(self):
        id = input("Entre com o ID do motorista: ")
        indice = int(input("Entre com o índice da corrida para alterar seus valores (começando de 1): ")) - 1  # Ajusta o índice para 0

        motora = self.motora_model.read_motora_by_id(id)
        if motora:
            corridas = motora.get('Corrida', [])  # Use 'Corrida' como chave
            if 0 <= indice < len(corridas):
                # Solicita os novos valores para a corrida
                print("Alterando a corrida:")
                nota = int(input(f"Entre com a nova nota (atual: {corridas[indice]['nota']}): ") or corridas[indice]['nota'])
                distancia = float(input(f"Entre com a nova distância (atual: {corridas[indice]['distancia']} km): ") or corridas[indice]['distancia'])
                valor = float(input(f"Entre com o novo valor (atual: R${corridas[indice]['valor']:.2f}): ") or corridas[indice]['valor'])
                
                # Solicita os dados do passageiro
                nome_passageiro = input(f"Nome do passageiro (atual: {corridas[indice]['passageiro']['nome']}): ") or corridas[indice]['passageiro']['nome']
                documento_passageiro = input(f"Documento do passageiro (atual: {corridas[indice]['passageiro']['documento']}): ") or corridas[indice]['passageiro']['documento']

                # Cria o novo objeto Passageiro
                passageiro = Passageiro.Passageiro(nome=nome_passageiro, documento=documento_passageiro)

                # Atualiza a corrida
                corridas[indice]['nota'] = nota
                corridas[indice]['distancia'] = distancia
                corridas[indice]['valor'] = valor
                corridas[indice]['passageiro'] = passageiro.to_dict()  # Atualiza os dados do passageiro
                
                # Solicita a nova nota geral do motorista
                nova_nota_motorista = int(input("Entre com a nova nota do motorista: "))
                
                # Atualiza o motorista no modelo
                self.motora_model.update_motora(id, nova_nota_motorista, corridas)  # Passa todos os argumentos necessários
                print("Corrida atualizada com sucesso!")
            else:
                print("Índice de corrida inválido.")
        else:
            print("Motorista não encontrado.")





    def delete_motora(self):
        id = input("Entre com o ID do motorista: ")
        
        # Verifica se o motorista existe antes de tentar excluir
        motora = self.motora_model.read_motora_by_id(id)
        if motora:
            # Executa a exclusão do motorista no banco de dados
            res = self.motora_model.delete_motora(id)
            
            if res:
                print("Motorista excluído com sucesso!")
            else:
                print("Não foi possível excluir o motorista.")
        else:
            print("Motorista não encontrado.")


        
    def run(self):
        print("Bem vindo ao CLI Motorista!")
        print("Comandos disponíveis: Inserir, Ler, Alterar, Excluir, Sair")
        super().run()
        
