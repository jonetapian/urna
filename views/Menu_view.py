from views.Urna_view import Urna_view
from views.Partido_view import Partido_view
from views.Candidato_view import Candidato_view
from controllers.Geral_controller import Geral_controller

class Menu_view:

    def __init__(self):
        self.__geral_controller = Geral_controller()
        self.__urna_view = Urna_view(self.__geral_controller)
        self.__partido_view = Partido_view(self.__geral_controller)
        self.__candidato_view = Candidato_view(self.__geral_controller)

    def tela_opcoes(self):
        print("Escolha a opção")
        print("1: Urna")
        print("2: Partido")
        print("3: Candidato")
        print("4: Eleitor")
        print("5: Voto")
        print("0: Sair")

        opcao_escolhida = int(input("Escolha a opção: "))

        if (opcao_escolhida == 1):
            self.__urna_view.tela_opcoes_urna()
        elif (opcao_escolhida == 2):
            self.__partido_view.tela_opcoes_partido()
        elif (opcao_escolhida == 3):
            self.__candidato_view.tela_opcoes_candidato()


    def sair(self):
        exit(0)

    @property
    def geral_controller(self):
        return self.__geral_controller

    @geral_controller.setter
    def geral_controller(self, geral_controller):
        self.__geral_controller = geral_controller

    @property
    def urna_view(self):
        return self.__urna_view

    @urna_view.setter
    def urna_view(self, urna_view):
        self.__urna_view = urna_view

    @property
    def partido_view(self):
        return self.__partido_view

    @partido_view.setter
    def partido_view(self, partido_view):
        self.__partido_view = partido_view

    @property
    def candidato_view(self):
        return self.__candidato_view

    @candidato_view.setter
    def candidato_view(self, candidato_view):
        self.__candidato_view = candidato_view
