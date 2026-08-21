#declaração de classe 
class gafanhoto:
    """
    essa classe cria um gafanhoto que é uma pessoa que tem nome e idade, para criar uma nova pessoa use,
    variavel = gafanhoto(nome, idade) #documentação de classe 
    """
    def __init__(self, n = "", i = ""): #metodo construtor
        # atributos de instancia
        self.nome = n
        self.idade = i

    #metodos de instancia
    def aniversario(self):
        self.idade = self.idade + 1

    def __str__(self):
        return f"{self.nome} é gafanhoto e tem {self.idade} anos de idade" # Dunder Method

    def __getstate__(self):
        return f"Estado: nome = {self.nome}; idade = {self.idade}"

#declaração de objetos (mexendo pelo metodo com passagem com parametros)
g1 = gafanhoto( "maria", 17)
g1.aniversario()
print(g1)

g2 = gafanhoto( 'mauro', 53)
g2.aniversario()
print(g2)

g3 = gafanhoto()
print(g3)


print(g1.__dict__) #atributo
print(g1.__getstate__()) #metodo
print(g1.__class__) #dunder attribute 

#doc tambem é dunder attribute 