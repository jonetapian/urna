import PySimpleGUI as sg

class Partido_cadastro_view():

    def __init__(self):
        layout = [
            [sg.Text('INFORME OS DADOS DO PARTIDO')],
            [sg.Text('Código do Partido', size=(15, 1)), sg.InputText('texto_codigo_p')],
            [sg.Text('Nome do Partido', size=(15, 1)), sg.InputText('texto_nome')],
            [sg.Text('Sigla do Partido', size=(15, 1)), sg.InputText('texto_sigla')],
            [sg.Submit(), sg.Cancel()]
        ]

        self.__window = sg.Window('PARTIDO').Layout(layout)

    def abrir_tela(self):
        button, values = self.__window.Read()
        print(button, values[0], values[1], values[2])
        self.__window.close()
