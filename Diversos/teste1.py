print("Olá, pense em uma das pessoas abaixo e eu vou adivinhar quem você pensou!")
print("\n1 - homem de ferro")
print("\n2 - viuva negra")
print("\n3 - homem aranha")
print("\n4 - hulk")

resposta = input("\nPronto? (s/n): ")
if resposta == "s":
    resposta2 = input("\nÉ um homem?(s/n): ")
    if resposta2 == "s":
        resposta3 = input("\nÉ um heroi muito forte?(s/n): ")
        if resposta3 == "s":
            print("\nVocê pensou no hulk!")
        else:
            resposta4 = input("\nÉ um heroi que voa?(s/n): ")
            if resposta4 == "s":
                print("\nVocê pensou no homem de ferro!")
            else:
                print("\nVocê pensou no homem aranha!")
    else:
        print("\nVocê pensou na viuva negra!")