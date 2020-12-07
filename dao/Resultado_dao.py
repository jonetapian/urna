from classes import Resultado
from dao.Abstract_dao import Abstract_dao


class Resultado_dao(Abstract_dao):
    def __init__(self):
        super().__init__('resultados.pkl')

    def add(self, resultado: Resultado):
        if (resultado is not None):
            super().add(resultado.codigo_r, resultado)

    def get(self, key: int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key: int):
        if isinstance(key, int):
            return super().remove(key)


