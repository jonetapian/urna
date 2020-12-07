import PySimpleGUI as sg
from controllers.Geral_controller import Geral_controller
from views.candidato.Candidato_cadastro_view import Candidato_cadastro_view

class Candidato_consulta_view():

    def __init__(self):
        self.__candidato_cadastro_view = Candidato_cadastro_view()

    def abrir_tela(self):
        while True:
            lista_candidatos = Geral_controller().candidato_controller.listar_candidatos()

            layout = [
                [sg.Text('CANDIDATOS')],
                [sg.Listbox(values=lista_candidatos, select_mode='single', size=(50, 3))],
                [sg.Button("NOVO"), sg.Button("ALTERAR"), sg.Button("EXCLUIR")]
            ]

            self.__window = sg.Window('PARTIDOS').Layout(layout)

            button, values = self.__window.Read()
            if button == "NOVO":
                window = self.__candidato_cadastro_view.abrir_tela()
                self.__window.close()
            elif button == "ALTERAR":
                candidato_alterar = values[0]
                if (candidato_alterar):
                    candidato_split = candidato_alterar[0].split(" - ")
                    window = self.__candidato_cadastro_view.abrir_edicao(int(candidato_split[0]))
                else:
                    sg.popup("Selecione um registro para alterar.")
                self.__window.close()
            elif button == "EXCLUIR":
                candidato_excluir = values[0]
                if (candidato_excluir):
                    candidato_split = candidato_excluir[0].split(" - ")
                    Geral_controller().candidato_controller.excluir_candidato(int(candidato_split[0]))
                else:
                    sg.popup("Selecione um registro para excluir.")
                self.__window.close()
            elif (button == sg.WIN_CLOSED or button == None):
                self.__window.close()
                break

    @property
    def candidato_cadastro_view(self):
        return self.__candidato_cadastro_view

    @candidato_cadastro_view.setter
    def candidato_cadastro_view(self, candidato_cadastro_view):
        self.__candidato_cadastro_view = candidato_cadastro_view