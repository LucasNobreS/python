soma = 0
qtd = 0
numero = float(input("digite um numero para somar: ",))
while numero > 0:
    soma = soma + numero
    qtd = qtd + 1
    numero = float(input("digite um numero para somar: ",));
media = soma / qtd
print("\na soma dos numeros digitados é: ", soma)
print("\n quantidade de numeros digitados é: ", qtd)
print("\n a media dos numeros digitados é: ", media)