def fatorial(numero):
    if numero > 0 and type(numero) == int:
        fatoria = 1
    for item in range (1, numero+1):
     fatoria = fatoria * item
    return fatoria

escolha = int(input("escolha um numero: "))
resultado = fatorial(escolha)
print(resultado)