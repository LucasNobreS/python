pnumero = float(input("Digite um numero: "))
snumero = float(input("Digite outro numero: "))

def somar (pnumero, snumero):
    resultado = pnumero + snumero
    return resultado

def subtrair (pnumero, snumero):
    resultado = pnumero - snumero
    return resultado

def dividir (pnumero, snumero):
    resultado = pnumero / snumero
    return resultado

def multiplicar (pnumero, snumero):
    resultado = pnumero * snumero
    return resultado

print("Escolha a operação \n-(+) \n-(-) \n-(/) \n-(x)")
escolha = input("Escolha uma opcao:")

if escolha == "+":
    print(f'o resultado é {somar(pnumero, snumero)}')
elif escolha == "-":
    print(f'o resultado é {subtrair(pnumero, snumero)}')
elif escolha == "/":
    print(f'o resultado é {dividir(pnumero, snumero)}')
else:
    print(f'o resultado é {multiplicar(pnumero, snumero)}')