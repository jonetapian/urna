import PySimpleGUI as sg
from controllers.Geral_controller import Geral_controller

class Partido_cadastro_view():

    def abrir_tela(self):
        layout = [
            [sg.Text('INFORME OS DADOS DO PARTIDO')],
            [sg.Text('Código do Partido', size=(15, 1)), sg.Input(key='CODIGO_P', enable_events=True)],
            [sg.Text('Nome do Partido', size=(15, 1)), sg.Input()],
            [sg.Text('Sigla do Partido', size=(15, 1)), sg.Input()],
            [sg.Text('Número do Partido', size=(15, 1)), sg.Input(key='NUMERO_P', enable_events=True)],
            [sg.Submit(), sg.Cancel()]
        ]

        self.__window = sg.Window('PARTIDO').Layout(layout)

        while True:
            event, values = self.__window.Read()

            if (event == 'CODIGO_P'):
                try:
                    if (values['CODIGO_P'] != ''):
                        int(values['CODIGO_P'])
                except:
                    sg.popup("O código do partido deve ser um número inteiro")
                    self.__window['CODIGO_P'].update('')
            elif (event == 'NUMERO_P'):
                try:
                    if (values['NUMERO_P'] != ''):
                        int(values['NUMERO_P'])
                except:
                    sg.popup("O número do partido deve ser um número inteiro")
                    self.__window['NUMERO_P'].update('')
            elif (event == 'Submit'):
                codigo_p = int(values['CODIGO_P'])
                texto_nome = values[0]
                texto_sigla = values[1]
                numero_p = int(values['NUMERO_P'])
                Geral_controller().partido_controller.salvar_partido(codigo_p, texto_nome, texto_sigla, numero_p)
                self.__window.close()
                break
            elif (event == sg.WIN_CLOSED or event == None or event == 'Cancel'):
                self.__window.close()
                break

    def abrir_edicao(self, codigo_partido):
        partido = Geral_controller().partido_controller.consultar_partido(codigo_partido)

        layout = [
            [sg.Text('INFORME OS DADOS DO PARTIDO')],
            [sg.Text('Código do Partido: ' + str(partido.codigo_p), size=(15, 1))],
            [sg.Text('Nome do Partido', size=(15, 1)), sg.InputText(partido.nome)],
            [sg.Text('Sigla do Partido', size=(15, 1)), sg.InputText(partido.sigla)],
            [sg.Text('Número do Partido', size=(15, 1)), sg.Input(str(partido.numero), key='NUMERO_P', enable_events=True)],
            [sg.Submit(), sg.Cancel()]
        ]

        self.__window = sg.Window('PARTIDO').Layout(layout)

        while True:
            event, values = self.__window.Read()

            if (event == 'NUMERO_P'):
                try:
                    if (values['NUMERO_P'] != ''):
                        int(values['NUMERO_P'])
                except:
                    sg.popup("O número do partido deve ser um número inteiro")
                    self.__window['NUMERO_P'].update(partido.numero)
            elif (event == 'Submit'):
                texto_nome = values[0]
                texto_sigla = values[1]
                numero_p = int(values['NUMERO_P'])
                Geral_controller().partido_controller.salvar_partido(partido.codigo_p, texto_nome, texto_sigla, numero_p)
                self.__window.close()
                break
            elif (event == sg.WIN_CLOSED or event == None or event == 'Cancel'):
                self.__window.close()
                break