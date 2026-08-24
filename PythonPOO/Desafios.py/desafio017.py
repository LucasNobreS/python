from rich.panel import Panel
from rich import print

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def etiqueta(self):
        etiquetas = Panel(f"            {self.nome}\n           R${self.preco: .2f}",title="Produto", width=35 )
        return etiquetas

p1 = Produto("notebook gamer", 8_000)
p2 = Produto("Iphone 17 pro max", 17_000)

print(p1.etiqueta())
print(p2.etiqueta())
