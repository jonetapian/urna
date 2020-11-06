from views.Geral_view import Geral_view

class Partido_view(Geral_view):

    def __init__(self, geral_controller):
        super().__init__(geral_controller)

    def tela_opcoes_partido(self):
        opcao_escolhida = super().tela_opcoes_especifca("Partido")

        if (opcao_escolhida == 1):
            self.incluir_partido()
        elif (opcao_escolhida == 2):
            self.alterar_partido()
        elif (opcao_escolhida == 3):
            self.excluir_partido()
        elif (opcao_escolhida == 4):
            self.listar_partidos()

    def incluir_partido(self):
        self.__texto_codigo_p = int(input("Digite o código para o Partido: "))
        self.__texto_nome = (input("Digite o nome do Partido: "))
        self.__texto_sigla = (input("Digite a sigla do Partido: "))
        self.__texto_numero = int(input("Digite o número do Partido: "))

        super().geral_controller.partido_controller.incluir_partido(self.__texto_codigo_p, self.__texto_nome, self.__texto_sigla, self.__texto_numero)

        print("-------- Partido cadastrado com sucesso! --------")

    def alterar_partido(self):
        self.__texto_codigo_p_alteracao = (input("Digite o código do Partido para alteração: "))
        print("Favor informar todos os novos dados do Partido: ")
        self.__texto_nome = (input("Digite o nome do Partido: "))
        self.__texto_sigla = (input("Digite a sigla do Partido: "))
        self.__texto_numero = (input("Digite o número do Partido: "))

        super().geral_controller.partido_controller.alterar_partido(self.__texto_codigo_p_alteracao, self.__texto_nome, self.__texto_sigla,
                                                  self.__texto_numero)

        print("------- Partido alterado com sucesso! -------")

    def excluir_partido(self):
        self.__texto_codigo_p = int(input("Informe o código do Partido a ser excluído: "))

        super().geral_controller.partido_controller.excluir_partido(self.__texto_codigo_p)

        print("------- Partido excluído com sucesso! --------")

    def listar_partidos(self):
        lista_partidos = super().geral_controller.partido_controller.listar_partidos()

        print("-----------------")
        print("Listando Partidos cadastrados")
        for i in range(len(lista_partidos)):
            print("Código Partido:", lista_partidos[i].codigo_p, "Nome: " + lista_partidos[i].nome,
                  "Sigla: " + lista_partidos[i].sigla, "Número do Partido:", lista_partidos[i].numero)

        print("-----------------")

    @property
    def texto_codigo_p(self):
        return self.__texto_codigo_p

    @texto_codigo_p.setter
    def texto_codigo_p(self, texto_codigo_p):
        self.__texto_codigo_p = texto_codigo_p

    @property
    def texto_codigo_p_alteracao(self):
        return self.__texto_codigo_p_alteracao

    @texto_codigo_p_alteracao.setter
    def texto_codigo_p_alteracao(self, texto_codigo_p_alteracao):
        self.__texto_codigo_p_alteracao = texto_codigo_p_alteracao

    @property
    def texto_nome(self):
        return self.__texto_nome

    @texto_nome.setter
    def texto_nome(self, texto_nome):
        self.__texto_nome = texto_nome

    @property
    def texto_sigla(self):
        return self.__texto_sigla

    @texto_sigla.setter
    def texto_sigla(self, texto_sigla):
        self.__texto_sigla = texto_sigla

    @property
    def texto_numero(self):
        return self.__texto_numero

    @texto_numero.setter
    def texto_numero(self, texto_numero):
        self.__texto_numero = texto_numero