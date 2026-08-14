nota1= float(input("Digite a primeira nota: "))
nota2= float(input("Digite a segunda nota: "))

media = (nota2+nota1)/2

if nota1 < 0 or nota1 > 10 or nota2 < 0 or nota2>10:
    print("Não é possivel digitar uma nota maior do que 10 ou menor do que zero")
elif media >= 7:
    print("Aluno Aprovado")
else:
    print("Aluno Reprovado")