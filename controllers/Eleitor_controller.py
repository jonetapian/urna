from classes.Eleitor import Eleitor
from dao.Eleitor_dao import Eleitor_dao

class Eleitor_controller:

    def __init__(self):
        self.eleitor_dao = Eleitor_dao()

    def salvar_eleitor(self, codigo_e, nome, nome_mae, numero_titulo, secao):
        novo_eleitor = Eleitor(codigo_e, nome, nome_mae, numero_titulo, secao)
        self.eleitor_dao.add(novo_eleitor)

    def excluir_eleitor(self,codigo_e):
        self.eleitor_dao.remove(codigo_e)

    def listar_eleitores(self):
        return self.eleitor_dao.get_all()

    def consultar_eleitor(self, codigo_eleitor):
        return self.eleitor_dao.get(codigo_eleitor)