from classes import Eleitor
from dao.Abstract_dao import Abstract_dao


class Eleitor_dao(Abstract_dao):
    def __init__(self):
        super().__init__('eleitores.pkl')

    def add(self, eleitor: Eleitor):
        if (eleitor is not None):
            super().add(eleitor.codigo_e, eleitor)

    def get(self, key: int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key: int):
        if isinstance(key, int):
            return super().remove(key)

    def get_all(self):
        lista_eleitores = super().get_all()
        lista_eleitores_string = []

        for eleitor in lista_eleitores:
            if (eleitor.codigo_e != None):
                eleitor_string = str(eleitor.codigo_e) + " - " + eleitor.nome
                lista_eleitores_string.append(eleitor_string)

        return lista_eleitores_string
