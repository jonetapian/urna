class Candidato():
    def __init__(self, codigo_c, nome, codigo_partido, cargo):
        self.__codigo_c = codigo_c
        self.__nome = nome
        self.__codigo_partido = codigo_partido
        self.__cargo = cargo

    @property
    def codigo_c(self):
        return self.__codigo_c

    @codigo_c.setter
    def codigo_c(self, codigo_c):
        self.__codigo_c = codigo_c

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

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