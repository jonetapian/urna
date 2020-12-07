from classes import Urna
from dao.Abstract_dao import Abstract_dao


class Urna_dao(Abstract_dao):
    def __init__(self):
        super().__init__('urnas.pkl')

    def add(self, urna: Urna):
        if (urna is not None):
            super().add(urna.codigo_u, urna)

    def get(self, key: int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key: int):
        if isinstance(key, int):
            return super().remove(key)

