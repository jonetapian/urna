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

    def get_all(self):
        lista_partidos = super().get_all()
        lista_partidos_string = []

        for partido in lista_partidos:
            if (partido.codigo_p != None):
                partido_string = str(partido.codigo_p) + " - " + partido.nome + " - " +  partido.sigla + " - " +  str(partido.numero)
                lista_partidos_string.append(partido_string)

        return lista_partidos_string
