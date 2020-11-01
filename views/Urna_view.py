from controlers.Urna_controller import Urna_controller

class Urna_view:

    def __init__(self):
        self.__urna_controller = Urna_controller()

    def tela_opcoes_urna(self):
        #lista_opcoes: {1: self.incluir_urna, 2: self.alterar_urna, 3: self.excluir_urna, 4: self.listar_urnas}

        print("Opções de Urna")
        print("1: Incluir")
        print("2: Alterar")
        print("3: Excluir")
        print("4: Listar")

        opcao_escolhida = int(input("Escolha a opção para Urna: "))

        if (opcao_escolhida == 1):
            self.incluir_urna()
        #funcao_escolhida = lista_opcoes[opcao_escolhida]

        #funcao_escolhida()

    def incluir_urna(self):
        print("Incluir Urna")

    def alterar_urna(self):
        print("Alterar Urna")

    def excluir_urna(self):
        print("Excluir Urna")

    def listar_urnas(self):
        print("Listar Urnas")






    @property
    def urna_controller(self):
        return self.__urna_controller

    @urna_controller.setter
    def urna_controller(self, urna_controller):
        self.__urna_controller = urna_controller

    @property
    def texto_codigo_u(self):
        return self.__texto_codigo_u

    @texto_codigo_u.setter
    def texto_codigo_u(self, texto_codigo_u):
        self.__texto_codigo_u = texto_codigo_u

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

    @property
    def texto_codigo_u_alteracao(self):
        return self.__texto_codigo_u_alteracao

    @texto_codigo_u_alteracao.setter
    def texto_codigo_u_alteracao(self, texto_codigo_u_alteracao):
        self.__texto_codigo_u_alteracao = texto_codigo_u_alteracao

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

