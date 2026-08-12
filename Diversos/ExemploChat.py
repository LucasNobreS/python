import os

mensagens = []

nome = input("Digite seu nome: ")

while True:

    os.system("cls")

    if len(mensagens) > 0:
        for m in mensagens:
            print(m["nome"], "-", m["texto"])
    print("______________")




    texto = input("Mensagem: ")
    if texto == "tchau":
        break


    mensagens.append({
        "nome": nome,
        "texto": texto
    })

    