from views.Geral_view import Geral_view
from utils.Validacao import *
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
        elif (opcao_escolhida == 0):
            return

    def incluir_candidato(self):
        lista_partidos = super().geral_controller.partido_controller.listar_partidos()
        if len(lista_partidos)  > 0 :
            self.__texto_codigo_c = validar_campo_digito("do codigo do candidato: ")
            if self.__texto_codigo_c < 1 or self.__texto_codigo_c > 98:
                print("Apenas numeros de 01 a 98 são validos")
                self.incluir_candidato()
            self.__texto_nome = (input("Digite o nome do Candidato: "))
            partido_valido = False
            while partido_valido == False:
                print("Cadastre um partido para o candidato")
                print("Os partidos cadastrados são")
                for partido in lista_partidos :
                    print("Nome - " + partido.nome + " - numero - " + str(partido.numero ))
                self.__texto_codigo_partido = validar_campo_digito("do codigo de partido do candidato: ")
                partido = super().geral_controller.partido_controller.consultar_partido(self.__texto_codigo_partido)
                if  partido != None:
                    partido_valido = True

            print("Escolha o cargo do candidato:")
            print("1: Prefeito")
            print("2: Vereador")
            cargo_valido  = False
            while cargo_valido == False:
                opcao = validar_campo_digito("da escolha :")
                if opcao == 1:
                    self.__texto_cargo = "Prefeito"
                    cargo_valido = True
                elif opcao == 2:
                    self.__texto_cargo = "Vereador"
                    cargo_valido = True
                
            super().geral_controller.candidato_controller.incluir_candidato(self.__texto_codigo_c, self.__texto_nome, self.__texto_codigo_partido,
                                                    self.__texto_cargo)

            print("-------- Candidato cadastrado com sucesso! --------")
            self.tela_opcoes_candidato()
        else :
            print("Para inserir um candidato é necessario adicionar um partido antes")
            print("--------------------------------")
            self.tela_opcoes_candidato()

    def alterar_candidato(self):
        self.__texto_codigo_c_alteracao = validar_campo_digito("do codigo do candidato para alteração: ")
        print("Favor informar todos os novos dados do Candidato: ")
        self.__texto_nome = (input("Digite o nome do Candidato: "))
        partido_valido = False
        while partido_valido == False:
            print("Cadastre um partido para o candidato")
            print("Os partidos cadastrados são")
            lista_partidos = super().geral_controller.partido_controller.listar_partidos()
            for partido in lista_partidos :
                print("Nome - " + partido.nome + " - numero - " + str(partido.numero ))
            self.__texto_codigo_partido = validar_campo_digito("do codigo de partido do candidato: ")
            partido = super().geral_controller.partido_controller.consultar_partido(self.__texto_codigo_partido)
            if  partido != None:
                partido_valido = True
        print("Escolha o cargo do candidato:")
        print("1: Prefeito")
        print("2: Vereador")
        cargo_valido  = False
        while cargo_valido == False:
            opcao = validar_campo_digito("da escolha :")
            if opcao == 1:
                self.__texto_cargo = "Prefeito"
                cargo_valido = True
            elif opcao == 2:
                self.__texto_cargo = "Vereador"
                cargo_valido = True
        super().geral_controller.candidato_controller.alterar_candidato(self.__texto_codigo_c_alteracao, self.__texto_nome, self.__texto_codigo_partido,
                                                  self.__texto_cargo)

        print("------- Candidato alterado com sucesso! -------")
        self.tela_opcoes_candidato()

    def excluir_candidato(self):
        self.__texto_codigo_c = validar_campo_digito("do codigo de candidato a ser excluido: ")

        super().geral_controller.candidato_controller.excluir_candidato(self.__texto_codigo_c)

        print("------- Candidato excluído com sucesso! --------")
        self.tela_opcoes_candidato()

    def listar_candidatos(self):
        lista_candidatos = super().geral_controller.candidato_controller.listar_candidatos()

        print("-----------------")
        print("Listando candidatos cadastrados")
        for i in range(len(lista_candidatos)):
            print("Código Candidato:", lista_candidatos[i].codigo_c, "Nome: " + lista_candidatos[i].nome,
                 "Cargo do candidato: " + lista_candidatos[i].cargo, "Código Partido: " + str(lista_candidatos[i].codigo_partido))

        print("-----------------")
        self.tela_opcoes_candidato()

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