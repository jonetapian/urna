class Voto_view():
    def __init__(self, geral_controller):
        self.__geral_controller = geral_controller
    
    def tela_opcoes_voto(self):
        print("Inicio de votação")
        opcao_vereador = self.votar_vereador()
        opcao_prefeito = self.votar_prefeito()
        self.__geral_controller.voto_controller.incluir_voto(opcao_vereador, opcao_prefeito)
        print("Fim da votação")
    def votar_vereador(self):
        self.listar_vereadores()
        opcao_vereador = int(input("Escolha a opção para votar: "))
        if self.__geral_controller.candidato_controller.checar_se_existe(opcao_vereador) == False:
            # raise
            i = 1
        else:
            return opcao_vereador
    def votar_prefeito(self):
        self.listar_prefeitos()
        opcao_prefeito = int(input("Escolha a opção para votar: "))
        if self.__geral_controller.candidato_controller.checar_se_existe(opcao_prefeito) == False:
            # raise
            f = 2
        else:
            return opcao_prefeito

    def listar_vereadores(self):
        print("--------------Vereadores-----------")
        for candidato in self.__geral_controller.candidato_controller.listar_vereadores():
            print("Nome -- " + candidato.nome + " -- Numero -- " + str(candidato.codigo_c))

    def listar_prefeitos(self):
        print("----------Prefeitos-------------")
        for candidato in self.__geral_controller.candidato_controller.listar_prefeitos():
            print("Nome --- " + candidato.nome + " -- Numero -- " + str(candidato.codigo_c))
