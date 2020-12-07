from controllers.Urna_controller import Urna_controller
from controllers.Partido_controller import Partido_controller
from controllers.Candidato_controller import Candidato_controller
from controllers.Eleitor_controller import Eleitor_controller
from controllers.Voto_controller import Voto_controller
from controllers.Resultado_controller import Resultado_controller

class Geral_controller:
    __instance = None

    def __init__(self):
        self.__urna_controller = Urna_controller()
        self.__partido_controller = Partido_controller()
        self.__candidato_controller = Candidato_controller()
        self.__eleitor_controller = Eleitor_controller()
        self.__voto_controller = Voto_controller()
        self.__resultado_controller = Resultado_controller()

    def __new__(cls):
        if Geral_controller.__instance is None:
            Geral_controller.__instance = object.__new__(cls)
        return Geral_controller.__instance

    @property
    def urna_controller(self):
        return self.__urna_controller

    @urna_controller.setter
    def urna_controller(self, urna_controller):
        self.__urna_controller = urna_controller

    @property
    def partido_controller(self):
        return self.__partido_controller

    @partido_controller.setter
    def partido_controller(self, partido_controller):
        self.__partido_controller = partido_controller

    @property
    def candidato_controller(self):
        return self.__candidato_controller

    @candidato_controller.setter
    def candidato_controller(self, candidato_controller):
        self.__candidato_controller = candidato_controller

    @property
    def eleitor_controller(self):
        return self.__eleitor_controller

    @eleitor_controller.setter
    def eleitor_controller(self, eleitor_controller):
        self.__eleitor_controller = eleitor_controller

    
    @property
    def voto_controller(self):
        return self.__voto_controller

    @voto_controller.setter
    def voto_controller(self, voto_controller):
        self.__voto_controller = voto_controller
    
    @property
    def resultado_controller(self):
        return self.__resultado_controller

    @resultado_controller.setter
    def resultado_controller(self, resultado_controller):
        self.__resultado_controller = resultado_controller
