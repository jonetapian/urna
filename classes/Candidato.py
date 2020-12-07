from classes.Pessoa import Pessoa

class Candidato(Pessoa):

    def __init__(self, codigo_c, nome, partido, cargo, numero_candidato):
        super().__init__(nome)
        self.__codigo_c = codigo_c
        self.__partido = partido
        self.__cargo = cargo
        self.__numero_candidato = numero_candidato

    @property
    def codigo_c(self):
        return self.__codigo_c

    @codigo_c.setter
    def codigo_c(self, codigo_c):
        self.__codigo_c = codigo_c

    @property
    def partido(self):
        return self.__partido

    @partido.setter
    def partido(self, partido):
        self.__partido = partido

    @property
    def cargo(self):
        return self.__cargo

    @cargo.setter
    def cargo(self, cargo):
        self.__cargo = cargo


        ## codigo partido vira partido , vai receber o objeto nao o codigoss
    @property
    def numero_candidato(self):
        return self.__numero_candidato

    @numero_candidato.setter
    def numero_candidato(self, numero_candidato):
        self.__numero_candidato = numero_candidato
