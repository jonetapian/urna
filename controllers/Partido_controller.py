from classes.Partido import Partido
from dao.Partido_dao import Partido_dao


class Partido_controller:

    def __init__(self):
        self.partido_dao = Partido_dao()

    def salvar_partido(self, codigo_p, nome, sigla, numero):
        novo_partido = Partido(codigo_p, nome, sigla, numero)
        self.partido_dao.add(novo_partido)

    def excluir_partido(self,codigo_p):
        self.partido_dao.remove(codigo_p)

    def listar_partidos(self):
        return self.partido_dao.get_all()

    def consultar_partido(self, codigo_partido):
        return self.partido_dao.get(codigo_partido)