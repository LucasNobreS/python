from rich import print
from rich import inspect

class Funcionario:
    #atributo de classe
    empresa = "Curso em Video"

    def __init__(self, nome, setor, cargo):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo

    def apresentacao(self):
        return f":handshake:Olá! Eu sou [blue]{self.nome}[/blue], e sou {self.cargo}  do setor de {self.setor} da empresa {Funcionario.empresa}"

c1 = Funcionario("Pedro", "TI", "Programador")
print(c1.apresentacao())