import PySimpleGUI as sg
from controllers.Geral_controller import Geral_controller
from views.urna.Urna_cadastro_view import Urna_cadastro_view

class Resultado_view():

    def __init__(self):
        pass
    def abrir_tela(self):
        self.buscar_urna_por_secao()
        self.abrir_votacao_prefeito()
        self.abrir_votacao_vereador()
        urna = Geral_controller().urna_controller.consultar_urna_por_secao(self.secao)
        Geral_controller().resultado_controller.incluir_resultado(self.numero_vereador, self.numero_prefeito, urna.codigo_u)
    def abrir_votacao_prefeito(self):
            layout = [
                [sg.Text('RESULTADO')],
                [sg.Listbox(values=lista_urnas, select_mode='single', size=(50, 3))],
                [sg.Button("NOVO"), sg.Button("ALTERAR"), sg.Button("EXCLUIR")]
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