from rich import print

class Funcionario:
    def __init__(self, nome, setor, cargo):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo

    def apresentacao(self):
        return f":hand:Olá! Eu sou [blue]{self.nome}[/blue], e sou {self.cargo}  do setor de {self.setor} da empresa curso em video"

c1 = Funcionario("Pedro", "TI", "Programador")
print(c1.apresentacao())