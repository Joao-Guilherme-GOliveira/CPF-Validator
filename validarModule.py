def limpar_cpf(cpf):
    cpf = str(cpf)
    cpf_limpo = cpf.replace(".","").replace("-","").replace(" ","")
    return cpf_limpo

def validar_tamanho(cpf):
    if len(cpf) == 11:
        resultado = True
    else:
        resultado = False
    return resultado
def valida_numero(cpf):
    if cpf == cpf[0] * len(cpf):
        return False
    else:
        return True
def calcular_digito(cpf, posicao):
    soma = 0
    for i in range(posicao - 1):
        soma+=int(cpf[i]) * posicao
        posicao -=1 

    resto = soma % 11
    if resto < 2:
        return 0
    else:
        return 11 - resto

def validar_cpf(cpf):
    resultado_final = limpar_cpf(cpf)

    if not validar_tamanho(resultado_final):
        return False
    
    primeiro_digito = calcular_digito(resultado_final,10)
    cpf_para_segundo = resultado_final[:9] + str(primeiro_digito)
    segundo_digito = calcular_digito(cpf_para_segundo,11)

    if not valida_numero(resultado_final):
        return False
    if primeiro_digito == int(resultado_final[9]) and segundo_digito == int(resultado_final[10]):
        return True
    else:
        return False
    
