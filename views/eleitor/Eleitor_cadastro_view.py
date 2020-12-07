import PySimpleGUI as sg
from controllers.Geral_controller import Geral_controller

class Eleitor_cadastro_view():

    def abrir_tela(self):
        layout = [
            [sg.Text('INFORME OS DADOS DO ELEITOR')],
            [sg.Text('Código do Eleitor', size=(23, 1)), sg.Input(key='CODIGO_E', enable_events=True)],
            [sg.Text('Nome do Eleitor', size=(23, 1)), sg.Input()],
            [sg.Text('Nome da mãe do Eleitor', size=(23, 1)), sg.Input()],
            [sg.Text('Número do Título do Eleitor', size=(23, 1)), sg.Input(key='NUMERO_TITULO', enable_events=True)],
            [sg.Text('Número da Seção Eleitoral', size=(23, 1)), sg.Input(key='NUMERO_SECAO', enable_events=True)],
            [sg.Submit(), sg.Cancel()]
        ]

        self.__window = sg.Window('ELEITOR').Layout(layout)

        while True:
            event, values = self.__window.Read()

            if (event == 'CODIGO_E'):
                try:
                    if (values['CODIGO_E'] != ''):
                        int(values['CODIGO_E'])
                except:
                    sg.popup("O código do eleitor deve ser um número inteiro")
                    self.__window['CODIGO_E'].update('')
            elif (event == 'NUMERO_TITULO'):
                try:
                    if (values['NUMERO_TITULO'] != ''):
                        int(values['NUMERO_TITULO'])
                except:
                    sg.popup("O número do título deve ser um número inteiro")
                    self.__window['NUMERO_TITULO'].update('')
            elif (event == 'NUMERO_SECAO'):
                try:
                    if (values['NUMERO_SECAO'] != ''):
                        int(values['NUMERO_SECAO'])
                except:
                    sg.popup("O número da seção deve ser um número inteiro")
                    self.__window['NUMERO_SECAO'].update('')
            elif (event == 'Submit'):
                codigo_e = int(values['CODIGO_E'])
                texto_nome = values[0]
                texto_nome_mae = values[1]
                numero_titulo = int(values['NUMERO_TITULO'])
                secao_eleitoral = int(values['NUMERO_SECAO'])
                Geral_controller().eleitor_controller.salvar_eleitor(codigo_e, texto_nome, texto_nome_mae, numero_titulo, secao_eleitoral)
                self.__window.close()
                break
            elif (event == sg.WIN_CLOSED or event == None or event == 'Cancel'):
                self.__window.close()
                break

    def abrir_edicao(self, codigo_eleitor):
        eleitor = Geral_controller().eleitor_controller.consultar_eleitor(codigo_eleitor)

        layout = [
            [sg.Text('INFORME OS DADOS DO ELEITOR')],
            [sg.Text('Código do Eleitor: ' + str(eleitor.codigo_e), size=(23, 1))],
            [sg.Text('Nome do Eleitor', size=(23, 1)), sg.InputText(eleitor.nome)],
            [sg.Text('Nome da mãe do Eleitor', size=(23, 1)), sg.InputText(eleitor.nome_mae)],
            [sg.Text('Número do Título do Eleitor', size=(23, 1)), sg.InputText(str(eleitor.numero_titulo), key='NUMERO_TITULO', enable_events=True)],
            [sg.Text('Número da Seção Eleitoral', size=(23, 1)), sg.InputText(str(eleitor.secao), key='NUMERO_SECAO', enable_events=True)],
            [sg.Submit(), sg.Cancel()]
        ]

        self.__window = sg.Window('ELEITOR').Layout(layout)

        while True:
            event, values = self.__window.Read()

            if (event == 'NUMERO_TITULO'):
                try:
                    if (values['NUMERO_TITULO'] != ''):
                        int(values['NUMERO_TITULO'])
                except:
                    sg.popup("O número do eleitor deve ser um número inteiro")
                    self.__window['NUMERO_TITULO'].update(eleitor.numero)
            elif (event == 'NUMERO_SECAO'):
                try:
                    if (values['NUMERO_SECAO'] != ''):
                        int(values['NUMERO_SECAO'])
                except:
                    sg.popup("O número da seção deve ser um número inteiro")
                    self.__window['NUMERO_SECAO'].update('')
            elif (event == 'Submit'):
                texto_nome = values[0]
                texto_nome_mae = values[1]
                numero_titulo = int(values['NUMERO_TITULO'])
                secao_eleitoral = int(values['NUMERO_SECAO'])
                Geral_controller().eleitor_controller.salvar_eleitor(eleitor.codigo_e, texto_nome, texto_nome_mae,
                                                                     numero_titulo, secao_eleitoral)
                self.__window.close()
                break
            elif (event == sg.WIN_CLOSED or event == None or event == 'Cancel'):
                self.__window.close()
                break