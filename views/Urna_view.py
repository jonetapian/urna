class Urna_view:
    
    def __init__(self, geral_controller):
        self.__geral_controller = geral_controller

    def tela_opcoes_urna(self):

        print("Opções de Urna")
        print("1: Incluir")
        print("2: Alterar")
        print("3: Excluir")
        print("4: Listar")

        opcao_escolhida = int(input("Escolha a opção para Urna: "))

        if (opcao_escolhida == 1):
            self.incluir_urna()
        elif (opcao_escolhida == 2):
            self.alterar_urna()
        elif (opcao_escolhida == 3):
            self.excluir_urna()
        elif (opcao_escolhida == 4):
            self.listar_urnas()

    def incluir_urna(self):
        self.__texto_codigo_u = int(input("Digite o código da Urna: "))
        self.__texto_estado_federativo = (input("Digite a sigla do Estado: "))
        self.__texto_municipio = (input("Digite o nome do município: "))
        self.__texto_zona_eleitoral = (input("Digite o número da Zona Eleitoral: "))
        self.__texto_secao_eleitoral = (input("Digite o número da Seção Eleitoral: "))
        self.__texto_turno = (input("Digite o Turno: "))
        self.__texto_data_homolgacao = (input("Digite a data da homolagação: "))
        self.__texto_data_encerramento = (input("Digite a data de encerramento: "))

        self.__geral_controller.urna_controller.incluir_urna(self.__texto_codigo_u, self.__texto_estado_federativo, self.__texto_municipio,
                                            self.__texto_zona_eleitoral, self.__texto_secao_eleitoral, self.__texto_turno,
                                            self.__texto_data_homolgacao, self.__texto_data_encerramento)

        print("-------- Urna cadastrada com sucesso! --------")

    def alterar_urna(self):
        self.__texto_codigo_u_alteracao = int(input("Digite o código da Urna para alteração: "))
        print("Favor informar todos os novos dados da Urna: ")
        self.__texto_estado_federativo = (input("Digite a sigla do Estado: "))
        self.__texto_municipio = (input("Digite o nome do município: "))
        self.__texto_zona_eleitoral = (input("Digite o número da Zona Eleitoral: "))
        self.__texto_secao_eleitoral = (input("Digite o número da Seção Eleitoral: "))
        self.__texto_turno = (input("Digite o Turno: "))
        self.__texto_data_homolgacao = (input("Digite a data da homolagação: "))
        self.__texto_data_encerramento = (input("Digite a data de encerramento: "))

        self.__geral_controller.urna_controller.alterar_urna(self.__texto_codigo_u_alteracao, self.__texto_estado_federativo, self.__texto_municipio,
                                            self.__texto_zona_eleitoral, self.__texto_secao_eleitoral, self.__texto_turno, self.__texto_data_homolgacao,
                                            self.__texto_data_encerramento)

        print("------- Urna alterada com sucesso! -------")

    def excluir_urna(self):
        self.__texto_codigo_u = int(input("Informe o código da urna a ser excluída: "))

        self.__geral_controller.urna_controller.excluir_urna(self.__texto_codigo_u )

        print("------- Urna excluída com sucesso! --------")

    def listar_urnas(self):
        lista_urnas = self.__geral_controller.urna_controller.listar_urnas()

        print("-----------------")
        print("Listando Urnas cadastradas")
        for i in range(len(lista_urnas)):
            print("Código Urna:", lista_urnas[i].codigo_u)
            print("Estado Federativo Urna: " + lista_urnas[i].estado_federativo)
            print("Município: " + lista_urnas[i].municipio)
            print("Zona Eleitoral: " + lista_urnas[i].zona)
            print("Seção Eleitoral: " + lista_urnas[i].secao)
            print("Turno: " + lista_urnas[i].turno)
            print("Data da Homologação: " + lista_urnas[i].data_homolgacao)
            print("Data do Encerramento: " + lista_urnas[i].data_encerramento)
        print("-----------------")

    @property
    def geral_controller(self):
        return self.__geral_controller

    @geral_controller.setter
    def geral_controller(self, geral_controller):
        self.__geral_controller = geral_controller

    @property
    def texto_codigo_u(self):
        return self.__texto_codigo_u

    @texto_codigo_u.setter
    def texto_codigo_u(self, texto_codigo_u):
        self.__texto_codigo_u = texto_codigo_u

    @property
    def texto_codigo_u_alteracao(self):
        return self.__texto_codigo_u_alteracao

    @texto_codigo_u_alteracao.setter
    def texto_codigo_u_alteracao(self, texto_codigo_u_alteracao):
        self.__texto_codigo_u_alteracao = texto_codigo_u_alteracao

    @property
    def texto_estado_federativo(self):
        return self.__texto_estado_federativo

    @texto_estado_federativo.setter
    def texto_estado_federativo(self, texto_estado_federativo):
        self.__texto_estado_federativo = texto_estado_federativo

    @property
    def texto_municipio(self):
        return self.__texto_municipio

    @texto_municipio.setter
    def texto_municipio(self, texto_municipio):
        self.__texto_municipio = texto_municipio

    @property
    def texto_zona_eleitoral(self):
        return self.__texto_zona_eleitoral

    @texto_zona_eleitoral.setter
    def texto_zona_eleitoral(self, texto_zona_eleitoral):
        self.__texto_zona_eleitoral = texto_zona_eleitoral

    @property
    def texto_secao_eleitoral(self):
        return self.__texto_secao_eleitoral

    @texto_secao_eleitoral.setter
    def texto_secao_eleitoral(self, texto_secao_eleitoral):
        self.__texto_secao_eleitoral = texto_secao_eleitoral

    @property
    def texto_turno(self):
        return self.__texto_turno

    @texto_turno.setter
    def texto_turno(self, texto_turno):
        self.__texto_turno = texto_turno

    @property
    def texto_data_homolgacao(self):
        return self.__texto_data_homolgacao

    @texto_data_homolgacao.setter
    def texto_data_homolgacao(self, texto_data_homolgacao):
        self.__texto_data_homolgacao = texto_data_homolgacao

    @property
    def texto_data_encerramento(self):
        return self.__texto_data_encerramento

    @texto_data_encerramento.setter
    def texto_data_encerramento(self, texto_data_encerramento):
        self.__texto_data_encerramento = texto_data_encerramento
