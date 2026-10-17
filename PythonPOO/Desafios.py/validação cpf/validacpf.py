
def valida_cpf(cpf):
    pos1=0
    pos2=0
    resultado=0
    for dig1 in range(10, 1, -1) :
        resultado += int(cpf[pos1])*dig1
        pos1 +=1
    if resultado % 11 == 0 or resultado%11 == 1:
        valido1 = 0
    elif resultado %11 > 1:
        valido1 = 11-(resultado%11)
    else: 
        print("Impossivel calcular!")
    if valido1 == int(cpf[9]):
        resultado = 0
        for dig2 in range(11, 1, -1) :
            resultado += int(cpf[pos2])*dig2
            pos2 +=1
        if resultado % 11 == 0 or resultado % 11 == 1:
            valido2 = 0
        elif resultado %11 >1:
            valido2 = 11-(resultado%11)
        else: 
            print("Impossivel calcular!")
    else: 
        print("cpf invalido!")

    if valido1 == int(cpf[9]) and valido2 == int(cpf[10]):
        print("CPF valido!")
    else:
        print("CPF invalido!")