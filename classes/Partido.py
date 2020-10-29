class Partido:
    def __init__(self, codigo_p, num_partido, nome, sigla):
        self.__codigo_p = codigo_p
        self.__num_partido = num_partido
        self.__nome = nome
        self.__sigla = sigla

    @property
    def codigo_p(self):
        return self.__codigo_p
    
    @codigo_p.setter
    def codigo_p(self,codigo_p):
        self.__codigo_p = codigo_p
    
    @property
    def num_partido(self):
        return self.__num_partido
    
    @num_partido.setter
    def num_partido(self, num_partido):
        self.__num_partido = num_partido

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


    
    
    
    

