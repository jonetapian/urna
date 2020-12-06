import PySimpleGUI as sg
from views.Urna_view import Urna_view
from views.Candidato_view import Candidato_view
from views.Eleitor_view import Eleitor_view
from controllers.Geral_controller import Geral_controller
from views.Voto_view import Voto_view
from views.Resultado_view import Resultado_view
from utils.Validacao import *
from views.partido.Partido_consulta_view import Partido_consulta_view


class Menu_view:

    def __init__(self):
        self.__geral_controller = Geral_controller()
        self.__urna_view = Urna_view(self.__geral_controller)
        self.__partido_consulta_view = Partido_consulta_view()
        self.__candidato_view = Candidato_view(self.__geral_controller)
        self.__eleitor_view = Eleitor_view(self.__geral_controller)
        self.__voto_view = Voto_view(self.__geral_controller)
        self.__resultado_view = Resultado_view(self.geral_controller)

        layout = [
            [sg.Text('OPÇÕES')],
            [sg.Button("URNA")],
            [sg.Button("PARTIDO")],
            [sg.Button("CANDIDATO")],
            [sg.Button("ELEITOR")],
            [sg.Button("VOTO")],
            [sg.Button("RESULTADO")],
            [sg.Button("SAIR")]
        ]
        self.__window = sg.Window('OPÇÕES').Layout(layout)

    def tela_opcoes(self):
        button, values = self.__window.Read()
        if (button == "URNA"):
            self.__urna_view.tela_opcoes_urna()
        elif (button == "PARTIDO"):
            self.__partido_consulta_view.abrir_tela()
        elif (button == "CANDIDATO"):
            self.__candidato_view.tela_opcoes_candidato()
        elif (button == "ELEITOR"):
            self.__eleitor_view.tela_opcoes_eleitor()
        elif (button == "VOTO"):
            self.__voto_view.tela_opcoes_voto()
        elif (button == "RESULTADO"):
            self.__resultado_view.tela_opcoes_resultado()
        elif (button == sg.WIN_CLOSED or button == 'SAIR'):
            return "SAIR"


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
    def partido_consulta_view(self):
        return self.__partido_consulta_view

    @partido_consulta_view.setter
    def partido_consulta_view(self, partido_consulta_view):
        self.__partido_consulta_view = partido_consulta_view

    @property
    def candidato_view(self):
        return self.__candidato_view

    @candidato_view.setter
    def candidato_view(self, candidato_view):
        self.__candidato_view = candidato_view

    @property
    def eleitor_view(self):
        return self.__eleitor_view

    @eleitor_view.setter
    def eleitor_view(self, eleitor_view):
        self.__eleitor_view = eleitor_view

    @property
    def voto_view(self):
        return self.__voto_view

    @voto_view.setter
    def voto_view(self, voto_view):
        self.__voto_view = voto_view
