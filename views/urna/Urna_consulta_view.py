import PySimpleGUI as sg
from controllers.Geral_controller import Geral_controller
from views.urna.Urna_cadastro_view import Urna_cadastro_view

class Urna_consulta_view():

    def __init__(self):
        self.__urna_cadastro_view = Urna_cadastro_view()

    def abrir_tela(self):
        while True:
            lista_urnas = Geral_controller().urna_controller.listar_urnas_como_str()
            layout = [
                [sg.Text('URNAS')],
                [sg.Listbox(values=lista_urnas, select_mode='single', size=(50, 3))],
                [sg.Button("NOVO"), sg.Button("ALTERAR"), sg.Button("EXCLUIR")]
            ]

            self.__window = sg.Window('URNAS').Layout(layout)

            button, values = self.__window.Read()
            if button == "NOVO":
                window = self.__urna_cadastro_view.abrir_tela()
                self.__window.close()
            elif button == "ALTERAR":
                urna_alterar = values[0]
                if (urna_alterar):
                    urna_split = urna_alterar[0].split(" - ")
                    window = self.__urna_cadastro_view.abrir_edicao(int(urna_split[0]))
                else:
                    sg.popup("Selecione um registro para alterar.")
                self.__window.close()
            elif button == "EXCLUIR":
                urna_excluir = values[0]
                if (urna_excluir):
                    urna_split = urna_excluir[0].split(" - ")
                    Geral_controller().urna_controller.excluir_urna(int(urna_split[0]))
                else:
                    sg.popup("Selecione um registro para excluir.")
                self.__window.close()
            elif (button == sg.WIN_CLOSED or button == None):
                self.__window.close()
                break

    @property
    def urna_cadastro_view(self):
        return self.__urna_cadastro_view

    @urna_cadastro_view.setter
    def urna_cadastro_view(self, urna_cadastro_view):
        self.__urna_cadastro_view = urna_cadastro_view