from classes.Candidato import Candidato

class Candidato_controller:

    def __init__(self):
        self.lista_candidatos = []

    def incluir_candidato(self, codigo_c, nome, codigo_partido, cargo):
        novo_candidato = Candidato(codigo_c, nome, codigo_partido, cargo)
        self.lista_candidatos.append(novo_candidato)

    def alterar_candidato(self, codigo_c_alteracao, nome, codigo_partido, cargo):
        novo_candidato = Candidato(codigo_c_alteracao, nome, codigo_partido, cargo)
        for i in range(len(self.lista_candidatos)):
            if self.lista_candidatos[i].codigo_c == codigo_c_alteracao:
                self.lista_candidatos[i] == novo_candidato

    def excluir_candidato(self, codigo_c):
        for i in range(len(self.lista_candidatos)):
            if self.lista_candidatos[i].codigo_c == codigo_c:
                self.lista_candidatos.pop(i)

    def listar_candidatos(self):
        return self.lista_candidatos

    def consultar_candidato(self, codigo_c):
        for i in range(len(self.lista_candidatos)):
            if self.lista_candidatos[i].codigo_c == codigo_c:
                return self.lista_candidatos[i]
