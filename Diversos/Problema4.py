#Problema: Gerenciador de login simples:
'''
Crie um gerenciador de login simples, com maximo de 3 tentativas (usuario e senha unicos).

usuario = "admin"
senha = "123456"

após 3 tentativas o programa deve exibir "aguarde 30 minutos antes de tentar novamente"
se o usuario e senha estiverem corretos, o programa deve exibir "login realizado com sucesso"
'''

usuario = ''
senha = ''
tentativas = 0

while (usuario != 'admin' or senha != '123') and tentativas < 3:
    usuario = input("Digite o usuario: ")
    senha = input("Digite a senha: ")
    tentativas += 1


if usuario != 'admin' or senha != '123':
    print("Aguarde 30 minutos antes de tentar novamente")
else:
    print("Login realizado com sucesso")