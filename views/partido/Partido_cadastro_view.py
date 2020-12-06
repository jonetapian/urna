import PySimpleGUI as sg
from controllers.Geral_controller import Geral_controller

class Partido_cadastro_view():

    def __init__(self):
        layout = [
            [sg.Text('INFORME OS DADOS DO PARTIDO')],
            [sg.Text('Código do Partido', size=(15, 1)), sg.InputText('')],
            [sg.Text('Nome do Partido', size=(15, 1)), sg.InputText('')],
            [sg.Text('Sigla do Partido', size=(15, 1)), sg.InputText('')],
            [sg.Text('Número do Partido', size=(15, 1)), sg.InputText('')],
            [sg.Submit(), sg.Cancel()]
        ]

        self.__window = sg.Window('PARTIDO').Layout(layout)

    def abrir_tela(self):
        button, values = self.__window.Read(close=True)
        texto_codigo_p = values[0]
        texto_nome = values[1]
        texto_sigla = values[2]
        texto_numero = values[3]

        Geral_controller().partido_controller.salvar_partido(texto_codigo_p, texto_nome, texto_sigla, texto_numero)



