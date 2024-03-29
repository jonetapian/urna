from classes.Candidato import Candidato
from dao.Candidato_dao import Candidato_dao

class Candidato_controller:

    def __init__(self):
        self.candidato_dao = Candidato_dao()

    def salvar_candidato(self, codigo_c, nome, codigo_partido, cargo, numero_candidato):
        novo_candidato = Candidato(codigo_c, nome, codigo_partido, cargo, numero_candidato)
        self.candidato_dao.add(novo_candidato)

    def excluir_candidato(self,codigo_c):
        self.candidato_dao.remove(codigo_c)

    def listar_candidatos(self):
        return self.candidato_dao.get_all()
    def listar_candidatos_como_str(self):
        return self.candidato_dao.get_all_as_str()

    def listar_prefeitos(self):
        prefeitos = []
        for candidato in self.listar_candidatos():
            if candidato.cargo == "Prefeito":
                prefeitos.append(candidato)
        return prefeitos

    def listar_vereadores(self):
        vereadores = []
        for candidato in self.listar_candidatos():
            if candidato.cargo == "Vereador":
                vereadores.append(candidato)
        return vereadores
    def consultar_candidato(self, codigo_candidato):
        return self.candidato_dao.get(codigo_candidato)
