from views.Urna_view import Urna_view

class Menu_view:

    def __init__ (self):
        self.__urna_view = Urna_view()

    def tela_opcoes(self):
        print("Escolha a opção")
        print("1: Urna")
        print("2: Partido")
        print("3: Candidato")
        print("4: Eleitor")
        print("5: Voto")
        print("0: Sair")

        opcao_escolhida = int(input("Escolha a opção: "))

        if (opcao_escolhida == 1):
            self.__urna_view.tela_opcoes_urna()
     #   elif (opcao_escolhida == 2):
     #       self.__partido_view.tela_opcoes_partido()

        return opcao_escolhida

    def sair(self):
        exit(0)



    #controlador
   # def abre_tela(self):

   #     lista_opcoes: {1: self.incluir_urna, 2: self.alterar_urna, 3: self.excluir_urna, 4: self.listar_urnas, 0: self.sair}

   #     opcao_escolhida = self.tela_opcoes()

   #     funcao_escolhida = lista_opcoes[opcao_escolhida]

  #      funcao_escolhida()

    @property
    def urna_view(self):
        return self.__urna_view

    @urna_view.setter
    def urna_view(self, urna_view):
        self.__urna_view = urna_view

 #   @property
 #   def partido_view(self):
 #       return self.partido_view

 #   @partido_view.setter
 #   def partido_view(self, partido_view):
  #      self.partido_view = partido_view
