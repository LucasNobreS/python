from rich.panel import Panel
from rich import print

class Churrasco:
    def __init__(self, quant, titulo):
        self.quant= quant
        self.titulo = titulo
        
    def analisar(self):
        preco = 400*(82.4 / 1000)
        consumo = preco * self.quant
        analise = Panel(f"Analisando o [green]{self.titulo}[/green] com [blue]{self.quant} convidados[/blue]\n Cada participante comerá 0.4kg de carne e cada kg custa R$82,40\n Recomendo comprar [blue]{ self.quant * 0.4}kg de carne[/blue]\n O custo total sera de R$[green]{consumo: .2f}[/green]\n Cada pessoa pagara [yellow]R${consumo / self.quant: .2f}[/yellow] para participar", width=45, title=self.titulo)
        return analise

c1 = Churrasco(15, "Churrasco")
print(c1.analisar())