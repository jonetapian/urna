from classes import Candidato
from dao.Abstract_dao import Abstract_dao


class Candidato_dao(Abstract_dao):
    def __init__(self):
        super().__init__('candidatos.pkl')

    def add(self, candidato: Candidato):
        if (candidato is not None):
            super().add(candidato.codigo_c, candidato)

    def get(self, key: int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key: int):
        if isinstance(key, int):
            return super().remove(key)

    def get_all_as_str(self):
        lista_candidatos = super().get_all()
        lista_candidatos_string = []

        for candidato in lista_candidatos:
            if (candidato.codigo_c != None):
                candidato_string = str(candidato.codigo_c) + " - " + candidato.nome + " - " + candidato.cargo + " - " + str(candidato.numero_candidato)
                lista_candidatos_string.append(candidato_string)

        return lista_candidatos_string
