import PySimpleGUI as sg
from controllers.Geral_controller import Geral_controller
from views.partido.Partido_cadastro_view import Partido_cadastro_view

class Partido_consulta_view():

    def __init__(self):
        self.__partido_cadastro_view = Partido_cadastro_view()

    def abrir_tela(self):
        while True:
            lista_partidos = Geral_controller().partido_controller.listar_partidos()

            layout = [
                [sg.Text('PARTIDOS')],
                [sg.Listbox(values=lista_partidos, select_mode='single', size=(50, 3))],
                [sg.Button("NOVO"), sg.Button("ALTERAR"), sg.Button("EXCLUIR")]
            ]

            self.__window = sg.Window('PARTIDOS').Layout(layout)

            button, values = self.__window.Read()
            if button == "NOVO":
                window = self.__partido_cadastro_view.abrir_tela()
                self.__window.close()
            elif button == "ALTERAR":
                partido_alterar = values[0]
                if (partido_alterar):
                    partido_split = partido_alterar[0].split(" - ")
                    window = self.__partido_cadastro_view.abrir_edicao(int(partido_split[0]))
                else:
                    sg.popup("Selecione um registro para alterar.")
                self.__window.close()
            elif button == "EXCLUIR":
                partido_excluir = values[0]
                if (partido_excluir):
                    partido_split = partido_excluir[0].split(" - ")
                    Geral_controller().partido_controller.excluir_partido(int(partido_split[0]))
                else:
                    sg.popup("Selecione um registro para excluir.")
                self.__window.close()
            elif (button == sg.WIN_CLOSED or button == None):
                self.__window.close()
                break

    @property
    def partido_cadastro_view(self):
        return self.__partido_cadastro_view

    @partido_cadastro_view.setter
    def partido_cadastro_view(self, partido_cadastro_view):
        self.__partido_cadastro_view = partido_cadastro_view