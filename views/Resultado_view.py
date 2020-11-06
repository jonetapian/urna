from utils.Validacao import *
class Resultado_view:
    def __init__(self, geral_controller):
        self.__geral_controller = geral_controller

    def tela_opcoes_resultado(self):
        print("-------- Resultados -----------")
        print("1: Ver prefeito eleito")
        print("2: Ver Lista Completa de prefeitos")
        print("3: Ver Vereador eleito")
        print("4: Ver Lista Completa de vereadores")

        print("0: Voltar para o menu principal")
        opcao = validar_campo_digito("da escolha :")
        if opcao == 1:
            self.mostar_prefeito_eleito()
        elif opcao == 2:
            self.mostrar_todos_prefeitos()
        elif opcao == 0:
            return
        elif opcao == 3:
            self.mostar_vereadores_eleitos()
        elif opcao == 4:
            self.mostrar_todos_vereadores()

    def mostar_vereadores_eleitos(self):
        lista_vereadores = self.__geral_controller.candidato_controller.listar_vereadores()
        lista_votos = self.__geral_controller.voto_controller.listar_votos()
        lista_partidos = self.__geral_controller.partido_controller.listar_partidos()
        lista_eleitos = self.__geral_controller.resultado_controller.listar_vereadores_eleitos(lista_vereadores, lista_votos, lista_partidos)
        for eleito in lista_eleitos:
            print("Eleito : " + eleito.candidato.nome + " numero de votos : " + str(eleito.numero_de_votos))
    
    def mostrar_todos_vereadores(self):
        lista_vereadores = self.__geral_controller.candidato_controller.listar_vereadores()
        lista_votos = self.__geral_controller.voto_controller.listar_votos()
        resultados = self.__geral_controller.resultado_controller.listar_votos_por_vereador(lista_vereadores, lista_votos)
        for resultado in resultados:
            print("Nome - " + resultado.candidato.nome + "-- Numero de votos - " + str(resultado.numero_de_votos))


    def mostar_prefeito_eleito(self):
        lista_prefeitos = self.__geral_controller.candidato_controller.listar_prefeitos()
        lista_votos = self.__geral_controller.voto_controller.listar_votos()
        resultados = self.__geral_controller.resultado_controller.listar_votos_por_prefeito(lista_prefeitos, lista_votos)
        eleito = resultados[0]
        print("Eleito : " + eleito.candidato.nome + " numero de votos : " + str(eleito.numero_de_votos))
    
    def mostrar_todos_prefeitos(self):
        lista_prefeitos = self.__geral_controller.candidato_controller.listar_prefeitos()
        lista_votos = self.__geral_controller.voto_controller.listar_votos()
        resultados = self.__geral_controller.resultado_controller.listar_votos_por_prefeito(lista_prefeitos, lista_votos)
        for resultado in resultados:
            print("Nome - " + resultado.candidato.nome + "-- Numero de votos - " + str(resultado.numero_de_votos))