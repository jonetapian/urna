from views.Geral_view import Geral_view
from utils.Validacao import *
class Eleitor_view(Geral_view):

    def __init__(self, geral_controller):
        super().__init__(geral_controller)

    def tela_opcoes_eleitor(self):
        opcao_escolhida = super().tela_opcoes_especifca("Eleitor")

        if (opcao_escolhida == 1):
            self.incluir_eleitor()
        elif (opcao_escolhida == 2):
            self.alterar_eleitor()
        elif (opcao_escolhida == 3):
            self.excluir_eleitor()
        elif (opcao_escolhida == 4):
            self.listar_eleitores()
        elif (opcao_escolhida == 0):
            return

    def incluir_eleitor(self):
        self.__texto_codigo_e = validar_campo_digito("do codigo do eleitor: ")
        self.__texto_nome = (input("Digite o nome do eleitor: "))
        self.__texto_nome_mae = (input("Digite o nome da mãe do eleitor: "))
        self.__texto_numero_titulo = validar_campo_digito("do título do eleitor: ")
        self.__texto_secao_eleitoral = validar_campo_digito("da seção eleitoral do eleitor: ")

        super().geral_controller.eleitor_controller.incluir_eleitor(self.__texto_codigo_e, self.__texto_nome, self.__texto_nome_mae,
                                                  self.__texto_numero_titulo, self.__texto_secao_eleitoral)

        print("-------- Eleitor cadastrado com sucesso! --------")
        self.tela_opcoes_eleitor()

    def alterar_eleitor(self):
        self.__texto_codigo_e_alteracao = validar_campo_digito("do codigo do eleitor para alteração: ")
        print("Favor informar todos os novos dados do eleitor: ")
        self.__texto_nome = (input("Digite o nome do eleitor: "))
        self.__texto_nome_mae = (input("Digite o nome da mãe do eleitor: "))
        self.__texto_numero_titulo = validar_campo_digito("do título do eleitor: ")
        self.__texto_secao_eleitoral = validar_campo_digito("da seção eleitoral do eleitor: ")

        super().geral_controller.eleitor_controller.alterar_eleitor(self.__texto_codigo_e_alteracao, self.__texto_nome, self.__texto_nome_mae,
                                                  self.__texto_numero_titulo, self.__texto_secao_eleitoral)

        print("------- Eleitor alterado com sucesso! -------")
        self.tela_opcoes_eleitor()

    def excluir_eleitor(self):
        self.__texto_codigo_e = validar_campo_digito("do codigo do eleitor para excluir: ")

        super().geral_controller.eleitor_controller.excluir_eleitor(self.__texto_codigo_e)

        print("------- Eleitor excluído com sucesso! --------")
        self.tela_opcoes_eleitor()

    def listar_eleitores(self):
        lista_eleitores = super().geral_controller.eleitor_controller.listar_eleitores()

        print("-----------------")
        print("Listando eleitores cadastrados")
        for i in range(len(lista_eleitores)):

            print("Código Eleitor:", str(lista_eleitores[i].codigo_e), "Nome: " + lista_eleitores[i].nome,
                  "Nome da mãe: " + lista_eleitores[i].nome_mae, "Número do título: " + str(lista_eleitores[i].numero_titulo),
                  "Número da Seção Eleitoral: " + str(lista_eleitores[i].secao))

        print("-----------------")
        self.tela_opcoes_eleitor()

    @property
    def texto_codigo_e(self):
        return self.__texto_codigo_e

    @texto_codigo_e.setter
    def texto_codigo_e(self, texto_codigo_e):
        self.__texto_codigo_e = texto_codigo_e

    @property
    def texto_codigo_e_alteracao(self):
        return self.__texto_codigo_e_alteracao

    @texto_codigo_e_alteracao.setter
    def texto_codigo_e_alteracao(self, texto_codigo_e_alteracao):
        self.__texto_codigo_e_alteracao = texto_codigo_e_alteracao

    @property
    def texto_nome(self):
        return self.__texto_nome

    @texto_nome.setter
    def texto_nome(self, texto_nome):
        self.__texto_nome = texto_nome

    @property
    def texto_nome_mae (self):
        return self.__texto_nome_mae

    @texto_nome_mae.setter
    def texto_nome_mae(self, texto_nome_mae):
        self.__texto_nome_mae  = texto_nome_mae

    @property
    def texto_numero_titulo(self):
        return self.__texto_numero_titulo

    @texto_numero_titulo.setter
    def texto_numero_titulo(self, texto_numero_titulo):
        self.__texto_numero_titulo = texto_numero_titulo

    @property
    def texto_secao_eleitoral(self):
        return  self.__texto_secao_eleitoral

    @texto_secao_eleitoral.setter
    def texto_secao_eleitoral(self, texto_secao_eleitoral):
        self.__texto_secao_eleitoral = texto_secao_eleitoral