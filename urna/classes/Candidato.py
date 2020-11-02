from classes.Pessoa import Pessoa

class Candidato(Pessoa):

    def __init__(self, codigo_c, nome, codigo_partido, cargo):
        super().__init__(nome)
        self.__codigo_c = codigo_c
        self.__codigo_partido = codigo_partido
        self.__cargo = cargo

    @property
    def codigo_c(self):
        return self.__codigo_c

    @codigo_c.setter
    def codigo_c(self, codigo_c):
        self.__codigo_c = codigo_c

    @property
    def codigo_partido(self):
        return self.__codigo_partido

    @codigo_partido.setter
    def codigo_partido(self, codigo_partido):
        self.__codigo_partido = codigo_partido

    @property
    def cargo(self):
        return self.__cargo

    @cargo.setter
    def cargo(self, cargo):
        self.__cargo = cargo