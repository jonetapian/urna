from classes.Partido import Partido

class Partido_controller:

    def __init__(self):
        self.lista_partidos = []
    
    def incluir_partido(self, codigo_p, nome, sigla, numero):
        novo_partido = Partido(codigo_p, nome, sigla, numero)
        self.lista_partidos.append(novo_partido)

    def alterar_partido(self,codigo_p_alteracao, nome, sigla, numero):
        novo_partido = Partido(codigo_p_alteracao, nome, sigla, numero)
        for i in range(len(self.lista_partidos)):
            if self.lista_partidos[i].codigo_p == codigo_p_alteracao:
                self.lista_partidos[i] == novo_partido

    def excluir_partido(self,codigo_p):
        for i in range(len(self.lista_partidos)):
            if self.lista_partidos[i].codigo_p == codigo_p:
                self.lista_partidos.pop(i)

    def listar_partidos(self):
        return self.lista_partidos

    def consultar_partido(self, numero_partido):
        for partido in self.lista_partidos:
            if partido.numero == numero_partido:
                return partido
        return None