import PySimpleGUI as sg
from controllers.Geral_controller import Geral_controller

class Urna_cadastro_view():

    def abrir_tela(self):
        layout = [
            [sg.Text('INFORME OS DADOS DA URNA')],
            [sg.Text('Código da urna', size=(15, 1)), sg.Input(key='CODIGO_U', enable_events=True)],
            [sg.Text('Estado federativo', size=(15, 1)), sg.Input()],
            [sg.Text('Munincípio', size=(15, 1)), sg.Input()],
            [sg.Text('Zona', size=(15, 1)), sg.Input(key='zona', enable_events=True)],
            [sg.Text('Seção', size=(15, 1)) , sg.Input(key='secao', enable_events=True)],
            [sg.Text('Turno', size=(15, 1)), sg.Combo(('Primeiro', 'Segundo'), size=(20, 1), readonly=True)],
            [sg.Text('Data de homologação', size=(15, 1)) , sg.Input()],
            [sg.Text('Data de encerramento', size=(15, 1)) , sg.Input()],
            [sg.Submit(), sg.Cancel()]
        ]


        self.__window = sg.Window('URNA').Layout(layout)

        while True:
            event, values = self.__window.Read()

            if (event == 'CODIGO_U'):
                try:
                    int(values['CODIGO_U'])
                except:
                    sg.popup("O código da urna deve ser um número inteiro")
                    self.__window['CODIGO_U'].update('')
            elif (event == 'zona'):
                try:
                    if (values['zona'] != ''):
                        int(values['zona'])
                except:
                    sg.popup("O número da zona deve ser um número inteiro")
                    self.__window['zona'].update('')
            elif (event == 'secao'):
                try:
                    if (values['secao'] != ''):
                        int(values['secao'])
                except:
                    sg.popup("O número da seção deve ser um número inteiro")
                    self.__window['secao'].update('')

            elif (event == 'Submit'):
                codigo_u = int(values['CODIGO_U'])
                Geral_controller().urna_controller.salvar_urna(codigo_u, values[0], values[1], int(values['zona']), int(values['secao']), values[2], values[3], values[4] )
                self.__window.close()
                break
            elif (event == sg.WIN_CLOSED or event == None or event == 'Cancel'):
                self.__window.close()
                break

    def abrir_edicao(self, codigo_urna):
        urna = Geral_controller().urna_controller.consultar_urna(codigo_urna)

        layout = [
            [sg.Text('INFORME OS DADOS DA URNA')],
            [sg.Text('Estado federativo', size=(15, 1)), sg.Input()],
            [sg.Text('Munincípio', size=(15, 1)), sg.Input()],
            [sg.Text('Zona', size=(15, 1)), sg.Input(key='zona', enable_events=True)],
            [sg.Text('Seção', size=(15, 1)) , sg.Input(key='secao', enable_events=True)],
            [sg.Text('Turno', size=(15, 1)), sg.Combo(('Primeiro', 'Segundo'), size=(20, 1), readonly=True)],
            [sg.Text('Data de homologação', size=(15, 1)) , sg.Input()],
            [sg.Text('Data de encerramento', size=(15, 1)) , sg.Input()],
            [sg.Submit(), sg.Cancel()]
        ]


        self.__window = sg.Window('URNA').Layout(layout)

        while True:
            event, values = self.__window.Read()

            if (event == 'zona'):
                try:
                    if (values['zona'] != ''):
                        int(values['zona'])
                except:
                    sg.popup("O número da zona deve ser um número inteiro")
                    self.__window['zona'].update('')
            elif (event == 'secao'):
                try:
                    if (values['secao'] != ''):
                        int(values['secao'])
                except:
                    sg.popup("O número da seção deve ser um número inteiro")
                    self.__window['secao'].update('')

            elif (event == 'Submit'):
                codigo_u = int(values['CODIGO_U'])
                Geral_controller().urna_controller.salvar_urna(codigo_u, values[0], values[1], int(values['zona']), int(values['secao']), values[2], values[3], values[4] )
                self.__window.close()
                break
            elif (event == sg.WIN_CLOSED or event == None or event == 'Cancel'):
                self.__window.close()
                break