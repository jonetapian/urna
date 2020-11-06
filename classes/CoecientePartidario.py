class Coenciente_partidario:
    def __init__(self,partido, numero_maximo_eleitos, numero_atual_eleitos):
        self.__partido = partido 
        self.__numero_maximo_eleitos = numero_maximo_eleitos
        self.__numero_atual_eleitos = numero_atual_eleitos
    
    @property
    def partido(self):
        return self.__partido

    @partido.setter
    def partido(self, partido):
        self.__partido = partido

    @property
    def numero_maximo_eleitos(self):
        return self.__numero_maximo_eleitos
    
    @numero_maximo_eleitos.setter
    def numero_maximo_eleitos(self, numero_maximo):
        self.__numero_maximo_eleitos = numero_maximo

    @property
    def numero_atual_eleitos(self):
        return self.__numero_atual_eleitos
    
    @numero_atual_eleitos.setter
    def numero_atual_eleitos(self, numero_atual):
        self.__numero_atual_eleitos = numero_atual

    