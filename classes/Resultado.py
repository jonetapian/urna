class Resultado():
    def __init__(self, candidato, numero_de_votos):
        self.__candidato = candidato
        self.__numero_de_votos = numero_de_votos
    @property
    def candidato(self):
        return self.__candidato
    @candidato.setter
    def candidato(self, candidato):
        self.__candidato = candidato

    @property
    def numero_de_votos(self):
        return self.__numero_de_votos
    @numero_de_votos.setter
    def numero_de_votos(self, numero_de_votos):
        self.__numero_de_votos = numero_de_votos

