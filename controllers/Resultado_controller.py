from classes.Resultado import Resultado
from classes.CoecientePartidario import Coenciente_partidario
class Resultado_controller:
    def __init__(self):
        pass

    def listar_vereadores_eleitos(self, lista_vereadores, lista_votos, lista_partidos):
        resultados = self.listar_votos_por_vereador(lista_vereadores, lista_votos)
        lista_quoociente = []
        lista_eleitos = []
        for partido in lista_partidos:
            total_votos_validos = 0 
            votos_validos_partido = 0
            for resultado in resultados:
                total_votos_validos += resultado.numero_de_votos
                if resultado.candidato.codigo_partido == partido.numero:
                    votos_validos_partido += resultado.numero_de_votos
            quociente_eleitoral = round(total_votos_validos / 3)
            quociente_partidario = round(votos_validos_partido / quociente_eleitoral)
            lista_quoociente.append(Coenciente_partidario(partido, quociente_partidario,0 ))
            for resultado in resultados:
                if resultado.candidato.codigo_partido == partido.codigo_p:
                    for quociente_eleitoral in lista_quoociente:
                        if quociente_eleitoral.partido.codigo_p == resultado.candidato.codigo_partido:
                            if quociente_eleitoral.numero_maximo_eleitos > quociente_eleitoral.numero_atual_eleitos:
                                lista_eleitos.append(resultado)
                                quociente_eleitoral.numero_atual_eleitos += 1

        return lista_eleitos
    def listar_votos_por_vereador(self, lista_vereadores, lista_votos):
        resultados = []
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
                if voto.numero_prefeito == candidato.codigo_c:
                    numero_de_votos += 1
            resultado = Resultado(candidato, numero_de_votos)
            resultados.append(resultado)
        resultados.sort(key=self.ordenar_votos, reverse=True)
        return resultados

    def listar_votos_vereador_branco(self, lista_votos):
        numero_de_votos_brancos = 0
        for voto in lista_votos:
            if voto.numero_vereador == 00:
                numero_de_votos_brancos += 1
        return numero_de_votos_brancos

    def listar_votos_vereador_invalido(self, lista_votos):
        numero_votos_invalidos =0
        for voto in lista_votos:
            if voto.numero_vereador == 99:
                numero_votos_invalidos += 1

        return numero_votos_invalidos

    def listar_votos_prefeito_branco(self, lista_votos):
        numero_de_votos_brancos = 0
        for voto in lista_votos:
            if voto.numero_prefeito == 00:
                numero_de_votos_brancos += 1
        return numero_de_votos_brancos

    def listar_votos_prefeito_invalido(self, lista_votos):
        numero_votos_invalidos =0
        for voto in lista_votos:
            if voto.numero_prefeito == 99:
                numero_votos_invalidos += 1
        return numero_votos_invalidos
    def ordenar_votos(self, elem):
        return elem.numero_de_votos
