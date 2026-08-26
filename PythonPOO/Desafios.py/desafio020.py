from rich.panel import Panel
from rich import print

class Gamer:
    def __init__(self, nome, nick):
        self.nome = nome
        self.nick = nick
        self.favoritos = list()

    def adicionar(self, game):
        self.favoritos.append(game)
        self.favoritos = sorted(self.favoritos, key=str.lower)

    def ficha(self):
        conteudo = f"Nome Real:[black on blue] {self.nome} [/]"
        conteudo += f"\nJogos favoritos: "
        for num, game in enumerate(self.favoritos):
            conteudo += f"\n:video_game: [blue]{game}[/]\n"
        painel = Panel(conteudo, title= f"Jogador <{self.nick}>", width=40)
        print(painel)

j1 = Gamer("Fabricio", "DetonaTudo123")
j1.adicionar("Sonic")
j1.adicionar("Mario Bros")
j1.adicionar("Minecraft")
j1.adicionar("God Of War")
j1.ficha()
