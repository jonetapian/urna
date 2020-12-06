from classes.Voto import Voto
from dao.Voto_dao import Voto_dao
class Voto_controller():
    def __init__(self):
        self.voto_dao = Voto_dao()

    def incluir_voto(self, numero_vereador, numero_prefeito, codigo_u):
        voto = Voto(numero_vereador, numero_prefeito, codigo_u)
        self.voto_dao.add(voto)
    
    def listar_votos(self):
        return self.voto_dao.get_all()
    

    
        