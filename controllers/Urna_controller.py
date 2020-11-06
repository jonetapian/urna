from classes.Urna import Urna

class Urna_controller:

    def __init__(self):
        self.lista_urnas = []
    
    def incluir_urna(self, codigo_u, estado_federativo, munincipio, zona, secao, turno, data_homologacao, data_encerramento):
        nova_urna = Urna(codigo_u, estado_federativo, munincipio, zona, secao, turno, data_homologacao, data_encerramento)
        self.lista_urnas.append(nova_urna)

    def alterar_urna(self, codigo_u_alteracao, estado_federativo, munincipio, zona, secao, turno, data_homologacao, data_encerramento ):
        nova_urna = Urna(codigo_u_alteracao, estado_federativo, munincipio, zona, secao, turno, data_homologacao, data_encerramento)
        for i in range(len(self.lista_urnas)):
            if self.lista_urnas[i].codigo_u == codigo_u_alteracao:
                self.lista_urnas.pop(i)
                self.lista_urnas.insert(i, nova_urna)

    def excluir_urna(self, codigo_u):
        for i in range(len(self.lista_urnas)):
            if self.lista_urnas[i].codigo_u == codigo_u:
                self.lista_urnas.pop(i)

    def listar_urnas(self):
        return self.lista_urnas

    def consultar_urna(self, codigo_u):
        for i in range(len(self.lista_urnas)):
            if self.lista_urnas[i].codigo_u == codigo_u:
                return self.lista_urnas[i]

    def consultar_urna_por_secao(self, secao):
        for urna in self.lista_urnas:
            if urna.secao == secao:
                return urna
        return None

    def secao_existe(self, secao_eleitoral):
        for urna in self.lista_urnas:
            if  urna.secao == secao_eleitoral:
                return True
        return False