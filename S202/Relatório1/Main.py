aluno = []
class Professor:
    def __init__(self, nome):
        self.nome = nome
    def ministrar_aula(self):
        print(f'O professor {self.nome} esta ministrando uma aula sobre {Aula.assunto}.')


class Aluno:
    def __init__(self, nome):
        self.nome = nome
    def presenca(self):
        print(f'O aluno {self.nome} esta presente.')


class Aula:
    def __init__(self, professor, assunto):
        self.professor = professor
        self.assunto = assunto
        self.alunos = []
    
    def adicionar_aluno(self, aluno):
        self.alunos.append(aluno)
    
    def listar_presenca(self):
        print(f'Presenca na aula sobre {self.assunto}, ministrada pelo professor {self.professor.nome}:')
        for aluno in self.alunos:
            aluno.presenca()

professor = Professor("Lucas")
aluno1 = Aluno("Maria")
aluno2 = Aluno("Pedro")
aula = Aula(professor, "Programacao Orientada a Objetos")
aula.adicionar_aluno(aluno1)
aula.adicionar_aluno(aluno2)
aula.listar_presenca()