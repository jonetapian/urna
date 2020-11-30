import PySimpleGUI as sg
from controllers.Geral_controller import Geral_controller
from views.partido import Partido_cadastro_view

class Partido_consulta_view():

    def __init__(self):
        geral_controller = Geral_controller()
        lista_partidos = geral_controller.partido_controller.listar_partidos()

        layout = [
            [sg.Text('PARTIDOS')],
            [sg.Listbox(values=['listbox1', 'listbox2', 'listbox3'], select_mode = 'single', size=(30,3))],
            [sg.Button("NOVO"), sg.Button("ALTERAR"), sg.Button("EXCLUIR")]
        ]

        self.__window = sg.Window('PARTIDOS').Layout(layout)

    def abrir_tela(self):
        button, values = self.__window.Read()
        if button == "NOVO":
            window = self.__partido_cadastro_view.abrir_tela()
        elif button == "ALTERAR":
            window = self.__partido_cadastro_view.abrir_tela()
        elif button == "EXCLUIR":
            partido_excluir = values[0]
            print(partido_excluir)


        print(button)
        self.__window.close()

    @property
    def partido_cadastro_view(self):
        return self.__partido_cadastro_view

    @partido_cadastro_view.setter
    def partido_cadastro_view(self, partido_cadastro_view):
        self.__partido_cadastro_view = partido_cadastro_view