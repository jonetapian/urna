
class Voto():
    def __init__(self,codigo_v, numero_vereador, numero_prefeito, codigo_u):
        self.__codigo_v = codigo_v
        self.__numero_vereador = numero_vereador
        self.__numero_prefeito = numero_prefeito

    @property
    def codigo_v(self):
        return self.__codigo_v

    @codigo_v.setter
    def codigo_v(self, codigo_v):
        self.codigo_v = codigo_v
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
    
    
    
