class Partido:
    def __init__(self, codigo_p, nome, sigla, numero):
        self.__codigo_p = codigo_p
        self.__nome = nome
        self.__sigla = sigla
        self.__numero = numero

    @property
    def codigo_p(self):
        return self.__codigo_p
    
    @codigo_p.setter
    def codigo_p(self,codigo_p):
        self.__codigo_p = codigo_p

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def sigla(self):
        return self.__sigla
    
    @sigla.setter
    def sigla(self,sigla):
        self.__sigla = sigla

    @property
    def numero(self):
        return self.__numero

    @numero.setter
    def numero(self, numero):
        self.__numero = numero


    
    
    
    

