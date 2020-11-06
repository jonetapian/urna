
def validar_campo_digito(str_detalhe):
    texto_valido = False

    while texto_valido == False:
        texto_para_validar = (input("Digite o número " + str_detalhe))
        if texto_para_validar.isdigit():
            texto_valido = True
            return texto_para_validar
        else:
            print("Informe novamente um número válido! ")
