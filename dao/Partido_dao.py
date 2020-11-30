from classes import Partido
from dao.Abstract_dao import Abstract_dao


class Partido_dao(Abstract_dao):
    def __init__(self):
        super().__init__('partidos.pkl')

    def add(self, partido: Partido):
        if (partido is not None):
            super().add(partido.codigo_p, partido)

    def get(self, key: int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key: int):
        if isinstance(key, int):
            return super().remove(key)