class Geral_view:

    def __init__(self, geral_controller):
        self.__geral_controller = geral_controller

    def tela_opcoes_especifca(self, tipo_view):
        print("Opções de " + tipo_view)
        print("1: Incluir")
        print("2: Alterar")
        print("3: Excluir")
        print("4: Listar")

        return int(input("Escolha a opção para " + tipo_view + ": "))

    @property
    def geral_controller(self):
        return self.__geral_controller

    @geral_controller.setter
    def geral_controller(self, geral_controller):
        self.__geral_controller = geral_controller