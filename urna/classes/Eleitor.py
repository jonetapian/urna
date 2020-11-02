from classes.Pessoa import Pessoa

class Eleitor(Pessoa):

    def __init__(self, codigo_e, nome, nome_mae, numero_titulo, secao):
        super().__init__(nome)
        self.__codigo_e = codigo_e
        self.__nome_mae = nome_mae
        self.__numero_titulo = numero_titulo
        self.__secao = secao

    @property
    def codigo_e(self):
        return self.__codigo_e

    @codigo_e.setter
    def codigo_e(self, codigo_e):
        self.__codigo_e = codigo_e

    @property
    def nome_mae(self):
        return self.__nome_mae

    @nome_mae.setter
    def nome_mae(self, nome_mae):
        self.__nome_mae = nome_mae

    @property
    def numero_titulo(self):
        return self.__numero_titulo

    @numero_titulo.setter
    def numero_titulo(self, numero_titulo):
        self.__numero_titulo = numero_titulo

    @property
    def secao(self):
        return self.__secao

    @secao.setter
    def secao(self, secao):
        self.__secao = secao