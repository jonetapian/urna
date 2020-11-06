from classes.Eleitor import Eleitor

class Eleitor_controller:

    def __init__(self):
        self.lista_eleitores = []

    def incluir_eleitor(self, codigo_e, nome, nome_mae, numero_titulo, secao):
        novo_eleitor = Eleitor(codigo_e, nome, nome_mae, numero_titulo, secao)
        self.lista_eleitores.append(novo_eleitor)

    def alterar_eleitor(self, codigo_e_alteracao, nome, nome_mae, numero_titulo, secao):
        novo_eleitor = Eleitor(codigo_e_alteracao, nome, nome_mae, numero_titulo, secao)
        for i in range(len(self.lista_eleitores)):
            if self.lista_eleitores[i].codigo_e == codigo_e_alteracao:
                self.lista_eleitores.pop(i)
                self.lista_eleitores.insert(i, novo_eleitor)

    def excluir_eleitor(self, codigo_e):
        for i in range(len(self.lista_eleitores)):
            if self.lista_eleitores[i].codigo_e == codigo_e:
                self.lista_eleitores.pop(i)

    def listar_eleitores(self):
        return self.lista_eleitores

    def listar_eleitor_por_secao(self, secao_eleitoral):
        lista_eleitores = self.lista_eleitores
        lista_eleitores_selecionados = []
        for eleitor in lista_eleitores:
            if eleitor.secao == secao_eleitoral:
                lista_eleitores_selecionados.append(eleitor)
        if len(lista_eleitores_selecionados) > 0:
            return lista_eleitores_selecionados
        else:
            return None
    

    def consultar_eleitor(self, codigo_e):
        for i in range(len(self.lista_eleitores)):
            if self.lista_eleitores[i].codigo_e == codigo_e:
                return self.lista_eleitores[i]
