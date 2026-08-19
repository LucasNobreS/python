import moeda as md

preco=float(input("Digite um preço: "))
print(f'O dobro de {preco} é {md.dobro(preco):.2f}')
print(f'A metade de {preco} é {md.metade(preco):.2f}')
print(f'Aumentando 10%, temos {md.aumentar(preco):.2f}')
print(f'Diminuindo 13%, temos {md.diminuir(preco):.2f}')

