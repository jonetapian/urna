from classes import Voto
from dao.Abstract_dao import Abstract_dao


class Voto_dao(Abstract_dao):
    def __init__(self):
        super().__init__('votos.pkl')

    def add(self, voto: Voto):
        if (voto is not None):
            super().add(voto.codigo_v, voto)

    def get(self, key: int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key: int):
        if isinstance(key, int):
            return super().remove(key)

    def get_all(self):
        lista_votos = super().get_all()
        lista_votos_string = []

        for voto in lista_votos:
            voto_string = voto.codigo_v + " - " + voto.numero_vereador + " - " +  voto.numero_prefeito
            lista_votos_string.append(voto_string)

        return lista_votos_string
