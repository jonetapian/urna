
class Voto():
    def __init__(self, numero_vereador, numero_prefeito, codigo_u):
        self.__codigo_u = codigo_u
        self.__numero_vereador = numero_vereador
        self.__numero_prefeito = numero_prefeito

    @property
    def codigo_u(self):
        return self.__codigo_u

    @codigo_u.setter
    def codigo_u(self, codigo_u):
        self.codigo_u = codigo_u
    @property
    def numero_vereador(self):
        return self.__numero_vereador
    
    @numero_vereador.setter
    def numero_vereador(self,numero_vereador):
        self.__numero_vereador = numero_vereador

    @property
    def numero_prefeito(self):
        return self.__numero_prefeito
    
    @numero_prefeito.setter
    def numero_prefeito(self,numero_prefeito):
        self.__numero_prefeito = numero_prefeito
    
    
    
