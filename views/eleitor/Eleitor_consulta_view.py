import PySimpleGUI as sg
from controllers.Geral_controller import Geral_controller
from views.eleitor.Eleitor_cadastro_view import Eleitor_cadastro_view

class Eleitor_consulta_view():

    def __init__(self):
        self.__eleitor_cadastro_view = Eleitor_cadastro_view()

    def abrir_tela(self):
        while True:
            lista_eleitores = Geral_controller().eleitor_controller.listar_eleitores()

            layout = [
                [sg.Text('ELEITORES')],
                [sg.Listbox(values=lista_eleitores, select_mode='single', size=(50, 3))],
                [sg.Button("NOVO"), sg.Button("ALTERAR"), sg.Button("EXCLUIR")]
            ]

            self.__window = sg.Window('ELEITORES').Layout(layout)

            button, values = self.__window.Read()
            if button == "NOVO":
                window = self.__eleitor_cadastro_view.abrir_tela()
                self.__window.close()
            elif button == "ALTERAR":
                eleitor_alterar = values[0]
                if (eleitor_alterar):
                    eleitor_split = eleitor_alterar[0].split(" - ")
                    window = self.__eleitor_cadastro_view.abrir_edicao(int(eleitor_split[0]))
                else:
                    sg.popup("Selecione um registro para alterar.")
                self.__window.close()
            elif button == "EXCLUIR":
                eleitor_excluir = values[0]
                if (eleitor_excluir):
                    eleitor_split = eleitor_excluir[0].split(" - ")
                    Geral_controller().eleitor_controller.excluir_eleitor(int(eleitor_split[0]))
                else:
                    sg.popup("Selecione um registro para excluir.")
                self.__window.close()
            elif (button == sg.WIN_CLOSED or button == None):
                self.__window.close()
                break

    @property
    def eleitor_cadastro_view(self):
        return self.__eleitor_cadastro_view

    @eleitor_cadastro_view.setter
    def eleitor_cadastro_view(self, eleitor_cadastro_view):
        self.__eleitor_cadastro_view = eleitor_cadastro_view