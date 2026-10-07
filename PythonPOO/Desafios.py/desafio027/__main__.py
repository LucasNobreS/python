from personagem_rpg import *

def main():
    p1 = Guerreiro(input("Digite o nome do personagem: "), int(input("Digite a vida do personagem: ")))
    p2 = Mago("Merlin", 5000)
    p3 = Guerreiro("Kratos", 1500)

    p1.atacar(p2)
    p2.atacar(p1)
    p1.curar()
    p2.curar()

if __name__ == "__main__":
    main()