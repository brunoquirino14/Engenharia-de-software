class TeacherCRUD:
    def __init__(self, database):
        self.db = database

    # cria professor
    def create(self, name, ano_nasc, cpf):
        query = "CREATE (:Professor {name: $name, ano_nasc: $ano_nasc, cpf: $cpf})"
        parameters = {"name": name, "ano_nasc": ano_nasc, "cpf": cpf}
        self.db.execute_query(query, parameters)

    # retorna resultado com base no nome
    def read(self, name):
        query = "MATCH (p: Professor{name: $name}) RETURN p.name AS nome, p.ano_nasc AS ano_nascimento, p.cpf AS CPF"
        parameters = {"name": name}
        results = self.db.execute_query(query, parameters)
        return [(result["nome"], result["ano_nascimento"], result["CPF"]) for result in results]

    # deleta um node com base no nome
    def delete(self, name):
        query = "MATCH (p: Professor{name: $name}) DETACH DELETE p"
        parameters = {"name": name}
        self.db.execute_query(query, parameters)

    # atualiza um node com base no nome, no caso do problema o cpf, mas poderia ser qualquer atributo
    def update(self, name, newCpf):
        query = "MATCH (p: Professor{name: $name}) SET p.cpf = $newCpf"
        parameters = {"name": name, "newCpf": newCpf}
        self.db.execute_query(query, parameters)

