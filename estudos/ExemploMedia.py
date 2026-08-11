nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = (nota1+nota2)/2
if media >= 5:
    print(f"Aprovado com média: {media:.1f} - aprovado")
else:
    print(f"Reprovado com média: {media:.1f} - reprovado")