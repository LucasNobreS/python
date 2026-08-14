numero1 = int(input("digite o primeiro numero: "))
numero2 = int(input("digite o segundo numero: "))
numero3 = int(input("digite o terceiro numero: "))

if numero1 > numero2 and numero1 > numero3:
    resultado = numero1
elif numero2 > numero1 and numero2 > numero3:
    resultado = numero2
elif numero3 > numero1 and numero3 > numero2:
    resultado = numero3
else:
    resultado = "os numeros sao iguais!"
print(f'o maior numero é {resultado}')