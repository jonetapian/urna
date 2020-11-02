from views.Geral_view import Geral_view

class Candidato_view(Geral_view):

    def __init__(self, geral_controller):
        super().__init__(geral_controller)

    def tela_opcoes_candidato(self):
        opcao_escolhida = super().tela_opcoes_especifca("Candidato")

        if (opcao_escolhida == 1):
            self.incluir_candidato()
        elif (opcao_escolhida == 2):
            self.alterar_candidato()
        elif (opcao_escolhida == 3):
            self.excluir_candidato()
        elif (opcao_escolhida == 4):
            self.listar_candidatos()

    def incluir_candidato(self):
        self.__texto_codigo_c = int(input("Digite o código para o Candidato: "))
        self.__texto_nome = (input("Digite o nome do Candidato: "))
        self.__texto_codigo_partido = int(input("Digite o código do partido do Candidato: "))
        self.__texto_cargo = (input("Digite o cargo do Candidato: "))

        super().geral_controller.candidato_controller.incluir_candidato(self.__texto_codigo_c, self.__texto_nome, self.__texto_codigo_partido,
                                                  self.__texto_cargo)

        print("-------- Candidato cadastrado com sucesso! --------")

    def alterar_candidato(self):
        self.__texto_codigo_c_alteracao = (input("Digite o código do Candidato para alteração: "))
        print("Favor informar todos os novos dados do Candidato: ")
        self.__texto_nome = (input("Digite o nome do Partido: "))
        self.__texto_codigo_partido = (input("Digite o código do partido do Candidato: "))
        self.__texto_cargo = (input("Digite o cargo do Candidato: "))

        super().geral_controller.candidato_controller.alterar_candidato(self.__texto_codigo_c_alteracao, self.__texto_nome, self.__texto_codigo_partido,
                                                  self.__texto_cargo)

        print("------- Candidato alterado com sucesso! -------")

    def excluir_candidato(self):
        self.__texto_codigo_c = int(input("Informe o código do Candidato a ser excluído: "))

        super().geral_controller.candidato_controller.excluir_candidato(self.__texto_codigo_c)

        print("------- Candidato excluído com sucesso! --------")

    def listar_candidatos(self):
        lista_candidatos = super().geral_controller.candidato_controller.listar_candidatos()

        print("-----------------")
        print("Listando candidatos cadastrados")
        for i in range(len(lista_candidatos)):
            partido_candidato = super().geral_controller.partido_controller.consultar_partido(lista_candidatos[i].codigo_partido)

            print("Código Candidato:", lista_candidatos[i].codigo_c, "Nome: " + lista_candidatos[i].nome,
                  "Sigla do Partido: " + partido_candidato.sigla, "Cargo do candidato: " + lista_candidatos[i].cargo)

        print("-----------------")

    @property
    def texto_codigo_c(self):
        return self.__texto_codigo_c

    @texto_codigo_c.setter
    def texto_codigo_c(self, texto_codigo_c):
        self.__texto_codigo_c = texto_codigo_c

    @property
    def texto_codigo_c_alteracao(self):
        return self.__texto_codigo_c_alteracao

    @texto_codigo_c_alteracao.setter
    def texto_codigo_c_alteracao(self, texto_codigo_c_alteracao):
        self.__texto_codigo_c_alteracao = texto_codigo_c_alteracao

    @property
    def texto_nome(self):
        return self.__texto_nome

    @texto_nome.setter
    def texto_nome(self, texto_nome):
        self.__texto_nome = texto_nome

    @property
    def texto_codigo_partido (self):
        return self.__texto_codigo_partido

    @texto_codigo_partido .setter
    def texto_codigo_partido(self, texto_codigo_partido):
        self.__texto_codigo_partido  = texto_codigo_partido

    @property
    def texto_cargo(self):
        return self.__texto_cargo

    @texto_cargo.setter
    def texto_cargo(self, texto_cargo):
        self.__texto_cargo = texto_cargo