import uteis as ut #tambem seria possivel escrever como: from uteis import fatorial, dobro, triplo. Nesse caso nao usar o uteis.dobro (ou ut)

num=int(input("Digite um numero: "))
fat=ut.fatorial(num)
print(f'o fatorial de {num} é {fat}')
print(f'o dobro de {num} é {ut.dobro(num)}')
print(f'o triplo de {num} é {ut.triplo(num)}')


