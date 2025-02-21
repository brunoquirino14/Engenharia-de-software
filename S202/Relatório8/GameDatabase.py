from neo4j import GraphDatabase

class GameDatabase:
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    # Método para criar jogador
    def create_player(self, player_id, name):
        with self.driver.session() as session:
            session.run("CREATE (p:Player {id: $player_id, name: $name})",
                        player_id=player_id, name=name)

    # Método para atualizar informações do jogador
    def update_player(self, player_id, name):
        with self.driver.session() as session:
            session.run("MATCH (p:Player {id: $player_id}) "
                        "SET p.name = $name",
                        player_id=player_id, name=name)

    # Método para excluir jogador
    def delete_player(self, player_id):
        with self.driver.session() as session:
            session.run("MATCH (p:Player {id: $player_id}) DETACH DELETE p",
                        player_id=player_id)

    # Método para listar jogadores
    def get_players(self):
        with self.driver.session() as session:
            result = session.run("MATCH (p:Player) RETURN p.id AS id, p.name AS name")
            return [{"id": record["id"], "name": record["name"]} for record in result]

    # Método para criar uma partida
    def create_match(self, match_id, player_ids, result):
        with self.driver.session() as session:
            session.run("CREATE (m:Match {id: $match_id, result: $result})",
                        match_id=match_id, result=result)
            for player_id in player_ids:
                session.run("MATCH (p:Player {id: $player_id}), (m:Match {id: $match_id}) "
                            "CREATE (p)-[:PLAYED]->(m)",
                            player_id=player_id, match_id=match_id)

    # Método para obter informações sobre uma partida
    def get_match(self, match_id):
        with self.driver.session() as session:
            result = session.run(
                "MATCH (m:Match {id: $match_id})<-[:PLAYED]-(p:Player) "
                "RETURN m.id AS id, m.result AS result, COLLECT(p.name) AS players",
                match_id=match_id)
            return result.single()

    # Método para registrar o resultado de uma partida
    def update_match_result(self, match_id, result):
        with self.driver.session() as session:
            session.run("MATCH (m:Match {id: $match_id}) "
                        "SET m.result = $result",
                        match_id=match_id, result=result)

    # Método para excluir uma partida
    def delete_match(self, match_id):
        with self.driver.session() as session:
            session.run("MATCH (m:Match {id: $match_id}) DETACH DELETE m",
                        match_id=match_id)

    # Método para obter histórico de partidas de um jogador
    def get_player_matches(self, player_id):
        with self.driver.session() as session:
            result = session.run(
                "MATCH (p:Player {id: $player_id})-[:PLAYED]->(m:Match) "
                "RETURN m.id AS match_id, m.result AS result",
                player_id=player_id)
            return [{"match_id": record["match_id"], "result": record["result"]} for record in result]

db = GameDatabase("bolt://44.195.37.158:7687", "neo4j", "slots-dedications-sail")
def main_menu():
    print("\n=== Menu do GameDatabase ===")
    print("1. Criar jogador")
    print("2. Atualizar jogador")
    print("3. Excluir jogador")
    print("4. Listar jogadores")
    print("5. Criar partida")
    print("6. Atualizar resultado de partida")
    print("7. Excluir partida")
    print("8. Ver informações de uma partida")
    print("0. Sair")

def main():
    # Instanciação do banco de dados
    db = GameDatabase("bolt://44.195.37.158:7687", "neo4j", "slots-dedications-sail")

    while True:
        main_menu()
        choice = input("Escolha uma opção: ")

        if choice == "1":  # Criar jogador
            player_id = input("Informe o ID do jogador: ")
            name = input("Informe o nome do jogador: ")
            db.create_player(player_id, name)
            print(f"Jogador '{name}' criado com sucesso.")

        elif choice == "2":  # Atualizar jogador
            player_id = input("Informe o ID do jogador: ")
            name = input("Informe o novo nome do jogador: ")
            db.update_player(player_id, name)
            print(f"Jogador com ID {player_id} atualizado com sucesso.")

        elif choice == "3":  # Excluir jogador
            player_id = input("Informe o ID do jogador: ")
            db.delete_player(player_id)
            print(f"Jogador com ID {player_id} excluído com sucesso.")

        elif choice == "4":  # Listar jogadores
            players = db.get_players()
            print("\n=== Lista de jogadores ===")
            for player in players:
                print(f"ID: {player['id']}, Nome: {player['name']}")

        elif choice == "5":  # Criar partida
            match_id = input("Informe o ID da partida: ")
            player_ids = input("Informe os IDs dos jogadores separados por vírgula: ").split(',')
            result = input("Informe o resultado da partida: ")
            db.create_match(match_id, player_ids, result)
            print(f"Partida '{match_id}' criada com sucesso.")

        elif choice == "6":  # Atualizar resultado de partida
            match_id = input("Informe o ID da partida: ")
            result = input("Informe o novo resultado da partida: ")
            db.update_match_result(match_id, result)
            print(f"Resultado da partida com ID {match_id} atualizado para '{result}'.")

        elif choice == "7":  # Excluir partida
            match_id = input("Informe o ID da partida: ")
            db.delete_match(match_id)
            print(f"Partida com ID {match_id} excluída com sucesso.")

        elif choice == "8":  # Ver informações de uma partida
            match_id = input("Informe o ID da partida: ")
            match = db.get_match(match_id)
            if match:
                print(f"\nPartida ID: {match['id']}")
                print(f"Resultado: {match['result']}")
                print(f"Jogadores: {', '.join(match['players'])}")
            else:
                print(f"Partida com ID {match_id} não encontrada.")

        elif choice == "0":  # Sair
            print("Encerrando o programa...")
            db.close()
            break

        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()

db.close()
