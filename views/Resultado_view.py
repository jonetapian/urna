class Resultado_view:
    def __init__(self, geral_controller):
        self.__geral_controller = geral_controller

    def tela_opcoes_resultado(self):
        print("-------- Resultados -----------")
        print("1 - para ver os resultados por prefeito")
        print("2 - para ver os resultados por vereador")
        opcao = int(input("Escolha uma opcao :"))
        if opcao == 1:
            lista_prefeitos = self.__geral_controller.candidato_controller.listar_prefeitos()
            lista_votos = self.__geral_controller.voto_controller.listar_votos()
            resultados = self.__geral_controller.resultado_controller.listar_votos_por_prefeito(lista_prefeitos, lista_votos)
            for resultado in resultados:
                print("Nome - " + resultado.candidato.nome + " Numero de votos -" + str(resultado.numero_de_votos))
        elif opcao == 2:
            lista_vereadores = self.__geral_controller.candidato_controller.listar_vereadores()
            lista_votos = self.__geral_controller.voto_controller.listar_votos()
            resultados = self.__geral_controller.resultado_controller.listar_votos_por_vereador(lista_vereadores, lista_votos)
            for resultado in resultados:
                print("Nome - " + resultado.candidato.nome + " Numero de votos -" + str(resultado.numero_de_votos))
