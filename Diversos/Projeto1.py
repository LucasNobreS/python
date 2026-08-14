numero = int(input("digite o numero que deseja saber o fatorial: "))
if numero > 0 and type(numero) == int:
    fatorial = 1
    for item in range (1, numero+1):
        print(f"{fatorial} * {item}")
        fatorial = fatorial * item
        print(f"{fatorial}")
        print(f"o fatorial de {numero} é {fatorial}!")
else:
    print("favor digitar somente numeros inteiros positivos")