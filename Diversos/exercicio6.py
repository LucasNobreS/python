numero = int(input("Digite um numero: "))
soma = 0 
quantidade = 0

while numero > 0:
    soma = soma + numero
    quantidade +=1
    numero = int(input("Digite um numero: "))

print(f'Quantidade: {quantidade}')
print(f'Soma: {soma}')
print(f'Media: {soma / quantidade}')