numero = int(input("Digite um número inteiro: "))


def primo(numero):
    if numero % numero == 0 and numero % 1 == 0:
        resultado = "é primo"
    elif numero % numero != 0 or numero % 1 != 0:
        resultado = "nao é primo"
    else: 
        resultado = "nao é inteiro"
    return (resultado)

print(f'o numero {numero} {primo(numero)}')