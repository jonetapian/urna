class Eleitor_view:

    def __init__(self, geral_controller):
        self.__geral_controller = geral_controller

    def tela_opcoes_eleitor(self):

        print("Opções de Eleitor")
        print("1: Incluir")
        print("2: Alterar")
        print("3: Excluir")
        print("4: Listar")

        opcao_escolhida = int(input("Escolha a opção para Eleitor: "))

        if (opcao_escolhida == 1):
            self.incluir_eleitor()
        elif (opcao_escolhida == 2):
            self.alterar_eleitor()
        elif (opcao_escolhida == 3):
            self.excluir_eleitor()
        elif (opcao_escolhida == 4):
            self.listar_eleitores()

    def incluir_eleitor(self):
        self.__texto_codigo_e = int(input("Digite o código para o Eleitor: "))
        self.__texto_nome = (input("Digite o nome do ELeitor: "))
        self.__texto_nome_mae = (input("Digite o nome da mãe do Eleitor: "))
        self.__texto_numero_titulo = (input("Digite o número do título: "))
        self.__texto_secao_eleitoral = (input("Digite o número da Seção Eleitoral: "))

        self.__geral_controller.eleitor_controller.incluir_eleitor(self.__texto_codigo_e, self.__texto_nome, self.__texto_nome_mae,
                                                  self.__texto_numero_titulo, self.__texto_secao_eleitoral)

        print("-------- Eleitor cadastrado com sucesso! --------")

    def alterar_eleitor(self):
        self.__texto_codigo_e_alteracao = (input("Digite o código do Eleitor para alteração: "))
        print("Favor informar todos os novos dados do Candidato: ")
        self.__texto_nome = (input("Digite o nome do ELeitor: "))
        self.__texto_nome_mae = int(input("Digite o nome da mãe do Eleitor: "))
        self.__texto_numero_titulo = (input("Digite o número do título: "))
        self.__texto_secao_eleitoral = (input("Digite o número da Seção Eleitoral: "))

        self.__geral_controller.eleitor_controller.alterar_eleitor(self.__texto_codigo_e_alteracao, self.__texto_nome, self.__texto_nome_mae,
                                                  self.__texto_numero_titulo, self.__texto_secao_eleitoral)

        print("------- Eleitor alterado com sucesso! -------")

    def excluir_eleitor(self):
        self.__texto_codigo_e = int(input("Informe o código do Eleitor a ser excluído: "))

        self.__geral_controller.eleitor_controller.excluir_eleitor(self.__texto_codigo_e)

        print("------- Eleitor excluído com sucesso! --------")

    def listar_eleitores(self):
        lista_eleitores = self.__geral_controller.eleitor_controller.listar_eleitores()

        print("-----------------")
        print("Listando eleitores cadastrados")
        for i in range(len(lista_eleitores)):

            print("Código Eleitor:", lista_eleitores[i].codigo_e, "Nome: " + lista_eleitores[i].nome,
                  "Nome da mãe: " + lista_eleitores[i].nome_mae, "Número do título: " + lista_eleitores[i].numero_titulo,
                  "Número da Seção Eleitoral: " + lista_eleitores[i].secao)

        print("-----------------")

    @property
    def geral_controller(self):
        return self.__geral_controller

    @geral_controller.setter
    def geral_controller(self, geral_controller):
        self.__geral_controller = geral_controller

    @property
    def texto_codigo_e(self):
        return self.__texto_codigo_e

    @texto_codigo_e.setter
    def texto_codigo_e(self, texto_codigo_e):
        self.__texto_codigo_e = texto_codigo_e

    @property
    def texto_codigo_e_alteracao(self):
        return self.__texto_codigo_e_alteracao

    @texto_codigo_e_alteracao.setter
    def texto_codigo_e_alteracao(self, texto_codigo_e_alteracao):
        self.__texto_codigo_e_alteracao = texto_codigo_e_alteracao

    @property
    def texto_nome(self):
        return self.__texto_nome

    @texto_nome.setter
    def texto_nome(self, texto_nome):
        self.__texto_nome = texto_nome

    @property
    def texto_nome_mae (self):
        return self.__texto_nome_mae

    @texto_nome_mae.setter
    def texto_nome_mae(self, texto_nome_mae):
        self.__texto_nome_mae  = texto_nome_mae

    @property
    def texto_numero_titulo(self):
        return self.__texto_numero_titulo

    @texto_numero_titulo.setter
    def texto_numero_titulo(self, texto_numero_titulo):
        self.__texto_numero_titulo = texto_numero_titulo

    @property
    def texto_secao_eleitoral(self):
        return  self.__texto_secao_eleitoral

    @texto_secao_eleitoral.setter
    def texto_secao_eleitoral(self, texto_secao_eleitoral):
        self.__texto_secao_eleitoral = texto_secao_eleitoral