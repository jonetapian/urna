import PySimpleGUI as sg
from controllers.Geral_controller import Geral_controller
from views.urna.Urna_cadastro_view import Urna_cadastro_view

class Resultado_view():

    def __init__(self):
        pass
    def abrir_tela(self):
        lista_prefeitos =  Geral_controller().candidato_controller.listar_prefeitos()
        lista_votos =  Geral_controller().voto_controller.listar_votos()
        resultados_prefeito =  Geral_controller().resultado_controller.listar_votos_por_prefeito(lista_prefeitos, lista_votos)
        candidatos_prefeito_str = []
        for resultado in resultados_prefeito:
            str_candidato = ("Nome - " + resultado.candidato.nome + "-- Numero de votos - " + str(resultado.numero_de_votos))
            candidatos_prefeito_str.append(str_candidato)



        lista_vereadores = Geral_controller().candidato_controller.listar_vereadores()
        resultados_vereador = Geral_controller().resultado_controller.listar_votos_por_vereador(lista_vereadores, lista_votos)
        candidatos_vereador_str = []
        for resultado in resultados_vereador:
            str_candidato = ("Nome - " + resultado.candidato.nome + "-- Numero de votos - " + str(resultado.numero_de_votos))
            candidatos_vereador_str.append(str_candidato)
        
        layout = [
                [sg.Text('RESULTADO')],
                [sg.Text('Prefeito eleito - ' + resultados_prefeito[0].candidato.nome)],
                [sg.Listbox(values=candidatos_prefeito_str, select_mode='single', size=(50, 3))],
                [sg.Text('Vereadores eleitos')],
                [sg.Listbox(values=candidatos_vereador_str, select_mode='single', size=(50, 3))],

            ]

        self.__window_resultado = sg.Window('Resultado').Layout(layout)
        button, values = self.__window_resultado.Read()
           
   