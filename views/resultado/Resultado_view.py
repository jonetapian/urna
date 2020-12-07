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
        lista_partidos = Geral_controller().partido_controller.listar_partidos()
        resultados_vereadores_eleitos = Geral_controller().resultado_controller.listar_vereadores_eleitos(lista_vereadores, lista_votos, lista_partidos )
        vereadores_eleitos_str = []
        for resultado in resultados_vereadores_eleitos:
            str_candidato = ("Nome - " + resultado.candidato.nome + "-- Numero de votos - " + str(resultado.numero_de_votos))
            vereadores_eleitos_str.append(str_candidato)
        resultados_vereadores = Geral_controller().resultado_controller.listar_votos_por_vereador(lista_vereadores, lista_votos)
        vereadores_str = []
        for resultado in resultados_vereadores:
            str_candidato = ("Nome - " + resultado.candidato.nome + "-- Numero de votos - " + str(resultado.numero_de_votos))
            vereadores_str.append(str_candidato)
        layout = [
                [sg.Text('RESULTADO')],
                [sg.Text('Prefeito eleito - ' + resultados_prefeito[0].candidato.nome)],
                [sg.Text('Todos os prefeitos')],
                [sg.Listbox(values=candidatos_prefeito_str, select_mode='single', size=(50, 3))],
                [sg.Text('Vereadores eleitos')],
                [sg.Listbox(values=vereadores_eleitos_str, select_mode='single', size=(50, 3))],
                [sg.Text('Todos os vereadores')],
                [sg.Listbox(values=vereadores_str, select_mode='single', size=(50, 3))],
            ]

        self.__window_resultado = sg.Window('Resultado').Layout(layout)
        button, values = self.__window_resultado.Read()
           
   