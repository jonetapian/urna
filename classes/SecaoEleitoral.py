class SecaoEleitoral
    def __init__(self, numero_secao, zona):
        self.__numero_secao = numero_secao
        self.__zona = zona
    
    @property
    def numero_secao(self):
        return self.__numero_secao
    
    @numero_secao.setter
    def codigo_p(self,numero_secao):
        self.__numero_secao = numero_secao
    
    @property
    def zona(self):
        return self.__zona
    
    @zona.setter
    def zona(self, zona):
        self.__zona = zona