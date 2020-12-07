from classes.Urna import Urna
from dao.Urna_dao import Urna_dao
class Urna_controller:

    def __init__(self):
        self.urna_dao = Urna_dao()

    def salvar_urna(self, codigo_u, estado_federativo, munincipio, zona, secao, turno, data_homologacao, data_encerramento):
        nova_urna = Urna(codigo_u, estado_federativo, munincipio, zona, secao, turno, data_homologacao, data_encerramento)
        self.urna_dao.add(nova_urna)

    def excluir_urna(self,codigo_u):
        self.urna_dao.remove(codigo_u)

    def listar_urnas(self):
        return self.urna_dao.get_all()

    def listar_urnas_como_str(self):
        lista_urnas = self.listar_urnas()
        lista_urnas_string = []
        for urna in lista_urnas:
            urna_string = str(urna.codigo_u) + " - " + urna.estado_federativo + " - " +  urna.munincipio + " - " + urna.zona + " - " + urna.secao + " - " + urna.turno + " - " + urna.data_homologacao + " - " + urna.data_encerramento    
            lista_urnas_string.append(urna_string)

        return lista_urnas_string

    def consultar_urna(self, codigo_u):
        return self.urna_dao.get(codigo_u)

    def consultar_urna_por_secao(self, secao):
        lista_urnas = self.listar_urnas()
        for urna in lista_urnas:
            if urna.secao == secao:
                return urna
        return None

    def secao_existe(self, secao_eleitoral):
        lista_urnas = self.listar_urnas()
        for urna in lista_urnas:
            if  urna.secao == secao_eleitoral:
                return True
        return False