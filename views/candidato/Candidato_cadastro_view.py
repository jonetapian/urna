import PySimpleGUI as sg
from controllers.Geral_controller import Geral_controller

class Candidato_cadastro_view():

    def abrir_tela(self):
        layout = [
            [sg.Text('INFORME OS DADOS DO CANDIDATO')],
            [sg.Text('Código do Candidato', size=(23, 1)), sg.Input(key='CODIGO_C', enable_events=True)],
            [sg.Text('Nome do Candidato', size=(23, 1)), sg.Input()],
            [sg.Text('Código do Partido', size=(23, 1)), sg.Input(key='CODIGO_PARTIDO', enable_events=True)],
            [sg.Text('Cargo', size=(23, 1)), sg.Combo(('Vereador', 'Prefeito'), size=(20, 1), readonly=True)],
            [sg.Text('Número do Candidato', size=(23, 1)), sg.Input(key='NUMERO', enable_events=True)],
            [sg.Submit(), sg.Cancel()]
        ]

        self.__window = sg.Window('CANDIDATO').Layout(layout)

        while True:
            event, values = self.__window.Read()

            if (event == 'CODIGO_C'):
                try:
                    int(values['CODIGO_C'])
                except:
                    sg.popup("O código do candidato deve ser um número inteiro")
                    self.__window['CODIGO_C'].update('')
            elif (event == 'CODIGO_PARTIDO'):
                try:
                    if (values['CODIGO_PARTIDO'] != ''):
                        codigo_partido = int(values['CODIGO_PARTIDO'])
                        partido = Geral_controller().partido_controller.consultar_partido(codigo_partido)
                        if (partido is None):
                            sg.popup("O código do partido deve referenciar um partido cadastrado")
                            self.__window['CODIGO_PARTIDO'].update('')
                except:
                    sg.popup("O número do código deve ser um número inteiro")
                    self.__window['CODIGO_PARTIDO'].update('')
            elif (event == 'NUMERO'):
                try:
                    if (values['NUMERO'] != ''):
                        int(values['NUMERO'])
                        qtde_digitos = len(values['NUMERO'])
                        if (values[1] != ''):
                            if (values[1] == 'Vereador' and qtde_digitos > 5):
                                sg.popup("O número de um Vereador deve conter 5 dígitos")
                                self.__window['NUMERO'].update('')
                            elif (values[1] == 'Prefeito' and qtde_digitos > 2):
                                sg.popup("O número de um Prefeito deve conter 2 dígitos")
                                self.__window['NUMERO'].update('')
                except:
                    sg.popup("O número do candidato deve ser um número inteiro")
                    self.__window['NUMERO'].update('')
            elif (event == 'Submit'):
                codigo_c = int(values['CODIGO_C'])
                texto_nome = values[0]
                codigo_partido = int(values['CODIGO_PARTIDO'])
                texto_cargo = values[1]
                numero_candidato = int(values['NUMERO'])
                qtde_digitos_numero_candidato = len(values['NUMERO'])

                validou = False

                if (texto_cargo != ''):
                    if (texto_cargo == 'Vereador' and qtde_digitos_numero_candidato != 5):
                        sg.popup("O número de um Vereador deve conter 5 dígitos")
                        self.__window['NUMERO'].update('')
                    elif (texto_cargo == 'Prefeito' and qtde_digitos_numero_candidato != 2):
                        sg.popup("O número de um Prefeito deve conter 2 dígitos")
                        self.__window['NUMERO'].update('')
                    else:
                        validou = True

                if(validou):
                    partido = Geral_controller().partido_controller.consultar_partido(codigo_partido)
                    Geral_controller().candidato_controller.salvar_candidato(codigo_c, texto_nome, partido, texto_cargo, numero_candidato)
                    self.__window.close()
                    break
            elif (event == sg.WIN_CLOSED or event == None or event == 'Cancel'):
                self.__window.close()
                break

    def abrir_edicao(self, codigo_candidato):
        candidato = Geral_controller().candidato_controller.consultar_candidato(codigo_candidato)

        layout = [
            [sg.Text('INFORME OS DADOS DO CANDIDATO')],
            [sg.Text('Código do Candidato: ' + str(candidato.codigo_c), size=(23, 1))],
            [sg.Text('Nome do Candidato', size=(23, 1)), sg.InputText(candidato.nome)],
            [sg.Text('Código do Partido', size=(23, 1)), sg.InputText(str(candidato.codigo_partido), key='CODIGO_PARTIDO', enable_events=True)],
            [sg.Text('Cargo', size=(23, 1)), sg.Combo(('Vereador', 'Prefeito'), candidato.cargo, size=(20, 1), readonly=True)],
            [sg.Text('Número do Candidato', size=(23, 1)), sg.Input(str(candidato.numero_candidato), key='NUMERO', enable_events=True)],
            [sg.Submit(), sg.Cancel()]
        ]

        self.__window = sg.Window('CANDIDATO').Layout(layout)

        while True:
            event, values = self.__window.Read()

            if (event == 'CODIGO_PARTIDO'):
                try:
                    if (values['CODIGO_PARTIDO'] != ''):
                        codigo_partido = int(values['CODIGO_PARTIDO'])
                        partido = Geral_controller().partido_controller.consultar_partido(codigo_partido)
                        if (partido is None):
                            sg.popup("O código do partido deve referenciar um partido cadastrado")
                            self.__window['CODIGO_PARTIDO'].update(candidato.codigo_partido)
                except:
                    sg.popup("O código do partido deve ser um número inteiro")
                    self.__window['CODIGO_PARTIDO'].update(candidato.codigo_partido)
            elif (event == 'NUMERO'):
                try:
                    if (values['NUMERO'] != ''):
                        int(values['NUMERO'])
                        qtde_digitos = len(values['NUMERO'])
                        if (values[1] != ''):
                            if (values[1] == 'Vereador' and qtde_digitos > 5):
                                sg.popup("O número de um Vereador deve conter 5 dígitos")
                                self.__window['NUMERO'].update(candidato.numero_candidato)
                            elif (values[1] == 'Prefeito' and qtde_digitos > 2):
                                sg.popup("O número de um Prefeito deve conter 2 dígitos")
                                self.__window['NUMERO'].update(candidato.numero_candidato)
                except:
                    sg.popup("O número do candidato deve ser um número inteiro")
                    self.__window['NUMERO'].update(candidato.numero_candidato)
            elif (event == 'Submit'):
                texto_nome = values[0]
                codigo_partido = int(values['CODIGO_PARTIDO'])
                texto_cargo = values[1]
                numero_candidato = int(values['NUMERO'])
                qtde_digitos_numero_candidato = len(values['NUMERO'])

                validou = False

                if (texto_cargo != ''):
                    if (texto_cargo == 'Vereador' and qtde_digitos_numero_candidato != 5):
                        sg.popup("O número de um Vereador deve conter 5 dígitos")
                        self.__window['NUMERO'].update('')
                    elif (texto_cargo == 'Prefeito' and qtde_digitos_numero_candidato != 2):
                        sg.popup("O número de um Prefeito deve conter 2 dígitos")
                        self.__window['NUMERO'].update('')
                    else:
                        validou = True

                if (validou):
                    Geral_controller().candidato_controller.salvar_candidato(candidato.codigo_c, texto_nome, codigo_partido, texto_cargo, numero_candidato)
                    self.__window.close()
                    break
            elif (event == sg.WIN_CLOSED or event == None or event == 'Cancel'):
                self.__window.close()
                break