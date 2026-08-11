def lernotas():
    n = float(input("Digite a nota: "))
    return n


def resultado(n1, n2):
    media = (n1 + n2) / 2

    print("Nota 1:", n1)
    print("Nota 2:", n2)
    print("Média:", media)

    if media >= 7:
        print("Resultado: Aprovado")
    else:
        print("Resultado: Reprovado")


a = lernotas()
b = lernotas()

resultado(a, b)