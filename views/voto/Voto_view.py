import PySimpleGUI as sg
from controllers.Geral_controller import Geral_controller
from views.urna.Urna_cadastro_view import Urna_cadastro_view

class Voto_view():

    def __init__(self):
        pass
    def abrir_tela(self):
        self.buscar_urna_por_secao()
        self.abrir_votacao_prefeito()
        self.abrir_votacao_vereador()
        urna = Geral_controller().urna_controller.consultar_urna_por_secao(self.secao)
        Geral_controller().voto_controller.incluir_voto(self.numero_vereador, self.numero_prefeito, urna.codigo_u)
    def abrir_votacao_prefeito(self):
            layout = [
                [sg.Text('INFORME O NUMERO DO PREFEITO')],
                [sg.Text('Número', size=(15, 1)) , sg.Input(key='numero', enable_events=True )],
                [sg.Submit(), sg.Cancel()]
            ]

            self.__window_prefeito = sg.Window('Votar para prefeito').Layout(layout)

            while True:
                event, values = self.__window_prefeito.Read()

                if (event == 'numero'):
                    try:
                        int(values['numero'])
                    except:
                        sg.popup("O número para votar deve ser um numero inteiro")
                        self.__window_prefeito['numero'].update('')
                elif (event == 'Submit'):
                    self.numero_prefeito = values['numero']
                    self.__window_prefeito.close()
                    break
                elif (event == sg.WIN_CLOSED or event == None or event == 'Cancel'):
                    self.__window_prefeito.close()
                    break


    def abrir_votacao_vereador(self):
            layout = [
                [sg.Text('INFORME O NUMERO DO VEREADOR')],
                [sg.Text('Número', size=(15, 1)) , sg.Input(key='numero', enable_events=True )],
                [sg.Submit(), sg.Cancel()]
            ]

            self.__window_vereador = sg.Window('Votar para vereador').Layout(layout)

            while True:
                event, values = self.__window_vereador.Read()

                if (event == 'numero'):
                    try:
                        int(values['numero'])
                    except:
                        sg.popup("O número para votar deve ser um numero inteiro")
                        self.__window_vereador['numero'].update('')
                elif (event == 'Submit'):
                    self.numero_vereador = values['numero']
                    self.__window_vereador.close()
                    break
                elif (event == sg.WIN_CLOSED or event == None or event == 'Cancel'):
                    self.__window_vereador.close()
                    break

    def buscar_urna_por_secao(self):
        layout = [
                    [sg.Text('INFORME A SUA SEÇÃO')],
                    [sg.Text('Número', size=(15, 1)) , sg.Input(key='secao', enable_events=True )],
                    [sg.Submit(), sg.Cancel()]
                ]

        self.__window_secao = sg.Window('SEÇÃO').Layout(layout)

        while True:
            event, values = self.__window_secao.Read()

            if (event == 'secao'):
                try:
                    int(values['secao'])
                except:
                    sg.popup("O número da seção deve ser um numero inteiro")
                    self.__window_secao['secao'].update('')
            elif (event == 'Submit'):
                self.secao = values['secao']
                self.__window_secao.close()
                break
            elif (event == sg.WIN_CLOSED or event == None or event == 'Cancel'):
                self.__window_secao.close()
                break
    @property
    def urna_cadastro_view(self):
        return self.__urna_cadastro_view

    @urna_cadastro_view.setter
    def urna_cadastro_view(self, urna_cadastro_view):
        self.__urna_cadastro_view = urna_cadastro_view

    @property
    def numero_prefeito(self):
        return self.__numero_prefeito
    
    @numero_prefeito.setter
    def numero_prefeito(self, numero):
        self.__numero_prefeito = numero
    @property
    def numero_vereador(self):
        return self.__numero_vereador
    
    @numero_vereador.setter
    def numero_vereador(self, numero):
        self.__numero_vereador = numero

    @property
    def secao(self):
        return self.__secao
    @secao.setter
    def secao(self, secao):
        self.__secao = secao