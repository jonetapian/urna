class Voto_view():
    def __init__(self, geral_controller):
        self.__geral_controller = geral_controller
    
    def tela_opcoes_voto(self):
        urna = self.buscar_urna_por_secao()
        if urna != None:
            if urna.data_homolagacao != None:
                print("Inicio de votação")
                opcao_vereador = self.votar_vereador()
                opcao_prefeito = self.votar_prefeito()
                self.__geral_controller.voto_controller.incluir_voto(opcao_vereador, opcao_prefeito, urna.codigo_u)
                print("Fim da votação")
            else:
                print("data da homologação não existe")
        else:
            print("Por favor digite uma seção valida")
            self.tela_opcoes_voto()

    def buscar_urna_por_secao(self):
        secao = int(input("Digite a sua seção eleitoral : "))
        return self.__geral_controller.urna_controller.consultar_urna_por_secao(secao)
    def votar_vereador(self):
        self.listar_vereadores()
        opcao_vereador = int(input("Escolha a opção para votar: "))
        if self.__geral_controller.candidato_controller.checar_se_existe(opcao_vereador) == False:
            if opcao_vereador == 0:
                return 00
            else:
                return 99
        else:
            return opcao_vereador
    def votar_prefeito(self):
        self.listar_prefeitos()
        opcao_prefeito = int(input("Escolha a opção para votar: "))
        if self.__geral_controller.candidato_controller.checar_se_existe(opcao_prefeito) == False:
            if opcao_prefeito == 0:
                return 00
            else:
                return 99
        else:
            return opcao_prefeito

    def listar_vereadores(self):
        print("--------------Vereadores-----------")
        print("---Escolha um numero para votar-----")
        print("0 - para votar em branco")
        for candidato in self.__geral_controller.candidato_controller.listar_vereadores():
            print("Nome -- " + candidato.nome + " -- Numero -- " + str(candidato.codigo_c))
    def listar_prefeitos(self):
        print("----------Prefeitos-------------")
        print("---Escolha um numero para votar-----")
        print("0 - para votar em branco")
        for candidato in self.__geral_controller.candidato_controller.listar_prefeitos():
            print("Nome --- " + candidato.nome + " -- Numero -- " + str(candidato.codigo_c))
