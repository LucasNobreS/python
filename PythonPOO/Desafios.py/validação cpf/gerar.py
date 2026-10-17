import random

def gerar_cpf():
    cpf = [random.randint(0, 9) for _ in range(9)]
    resultado = 0
    pesos1 = range(10, 1, -1)
    for i in range(9):
        resultado += cpf[i] * pesos1[i]
        
    resto1 = resultado % 11
    valido1 = 0 if resto1 < 2 else 11 - resto1
    cpf.append(valido1)
    
    resultado = 0
    pesos2 = range(11, 1, -1)
    for i in range(10):
        resultado += cpf[i] * pesos2[i]
        
    resto2 = resultado % 11
    valido2 = 0 if resto2 < 2 else 11 - resto2
    cpf.append(valido2)
    
    cpf_string = f"{cpf[0]}{cpf[1]}{cpf[2]}.{cpf[3]}{cpf[4]}{cpf[5]}.{cpf[6]}{cpf[7]}{cpf[8]}-{cpf[9]}{cpf[10]}"
    return cpf_string