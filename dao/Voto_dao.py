from classes import Voto
from dao.Abstract_dao import Abstract_dao


class Voto_dao(Abstract_dao):
    def __init__(self):
        super().__init__('votos.pkl')

    def add(self, voto: Voto):
        if (voto is not None):
            len_votos = len(super().cache)
            super().add(len_votos + 1, voto)

    def get(self, key: int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key: int):
        if isinstance(key, int):
            return super().remove(key)


