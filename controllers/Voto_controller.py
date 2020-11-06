from classes.Voto import Voto

class Voto_controller():
    def __init__(self):
        self.lista_votos = []

    def incluir_voto(self, numero_vereador, numero_prefeito, codigo_u):
        voto = Voto(numero_vereador, numero_prefeito, codigo_u)
        self.lista_votos.append(voto)
    
    def listar_votos(self):
        return self.lista_votos
    

    
        