from classes.Resultado import Resultado
class Resultado_controller:
    def __init__(self):
        pass

    def listar_votos_por_vereador(self, lista_vereadores, lista_votos):
        resultados = []
        validos = 0 
        brancos = 0
        for candidato in lista_vereadores:
            numero_de_votos = 0
            for voto in lista_votos:
                if voto.numero_vereador == candidato.codigo_c:
                    numero_de_votos += 1
            resultado = Resultado(candidato, numero_de_votos)
            resultados.append(resultado)
        resultados.sort(key=self.ordenar_votos, reverse= True)
        return resultados
    
    def listar_votos_por_prefeito(self, lista_prefeitos, lista_votos):
        resultados = []
        for candidato in lista_prefeitos:
            numero_de_votos = 0
            for voto in lista_votos:
                if voto.numero_vereador == candidato.codigo_c:
                    numero_de_votos += 1
            resultado = Resultado(candidato, numero_de_votos)
            resultados.append(resultado)
        resultados.sort(key=self.ordenar_votos, reverse=True)
        return resultados

    def ordenar_votos(self, elem):
        return elem.numero_de_votos