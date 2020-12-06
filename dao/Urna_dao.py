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

    def get_all(self):
        lista_urnas = super().get_all()
        lista_urnas_string = []

        for urna in lista_urnas:
            urna_string = urna.codigo_u + " - " + urna.estado_federativo + " - " +  urna.munincipio + " - " + urna.zona + " - " + urna.secao + " - " + urna.turno + " - " + urna.data_homologacao + " - " + urna.data_encerramento    
            lista_urnas_string.append(urna_string)

        return lista_urnas_string
