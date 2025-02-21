import Corrida


class Motorista:
    def __init__(self, corridas: Corrida, nota: int = 0):
        self.corridas = corridas
        self.nota = nota