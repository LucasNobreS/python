tentativa=0

while tentativa < 3:
    print("tentativa valida!")
    tentativa = tentativa + 1
print("tentativa invalida!")


senha= ''

while senha != '123456': #!= sinal de diferente
    senha = input("digite a senha: ")
print("senha correta!")


nome = ''
while nome == '':
    nome = input("Digite seu nome: ")
print("Bem vindo ao sistema", nome)

#contadores no while

horas = 0
while horas <= 17:
    print("Faltam", 17 - horas, "horas para o por do sol")
    horas = horas + 1
print("Hora do por do sol!")