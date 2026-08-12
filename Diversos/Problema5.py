salarios= [1000, 2000, 3000, 4000]

quantidade = len(salarios)
salario = 0 

if quantidade < 2:
    print("quantidade de salarios insuficiente")
else:
    for pos in range( quantidade):
        salario = salarios[pos] + salario
    print(salario)

#ou entao:

salarios= [1000, 2000, 3000, 4000]
total = 0

for salario in salarios:
    total = total + salario
print(total)