#declaração de classe 
class gafanhoto:
    def __init__(self): #metodo construtor
        # atributos de instancia
        self.nome = ""
        self.idade = 0

    #metodos de instancia
    def aniversario(self):
        self.idade = self.idade + 1

    def mensagem(self):
        return f"{self.nome} é gafanhoto e tem {self.idade} anos de idade"

#declaração de objetos
g1 = gafanhoto()
g1.nome = "maria"
g1.idade = 17
g1.aniversario()
print(g1.mensagem())

g2 = gafanhoto()
g2.nome = "Mauro"
g2.idade = 56
g2.aniversario()
print(g2.mensagem())

g3 = gafanhoto()
print(g3.mensagem())