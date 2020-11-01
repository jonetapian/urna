from controllers.Urna_controller import Urna_controller
from controllers.Partido_controller import Partido_controller
from controllers.Candidato_controller import Candidato_controller

class Geral_controller:

    def __init__(self):
        self.__urna_controller = Urna_controller()
        self.__partido_controller = Partido_controller()
        self.__candidato_controller = Candidato_controller()

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
