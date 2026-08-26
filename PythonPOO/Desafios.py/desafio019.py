from rich import print
import time

class Livro:
    def __init__(self, titulo, paginas):
        self.titulo = titulo
        self.totalp = paginas
        self.paginaat = 1

        print(f":open_book: [blue]você acabou de abrir o livro [red]'{self.titulo}'[/red] que tem [green]{self.totalp}[/green] paginas no total. Você agora esta na pagina [yellow]{self.paginaat}[/yellow][/blue]")

    def avancar(self, qtd = 1):
        cont = 0
        for pg in range(0, qtd, 1):
            if not self.fimlivro():
                self.paginaat += 1
                print(f"Pág{self.paginaat} :arrow_forward: ",end='')
                time.sleep(0.2)
                cont += 1
        print(f"[blue]Voce avançou {cont} paginas e agora esta na [yellow]pagina {self.paginaat}[/][/blue]")
        if self.fimlivro():
            print(f" :closed_book: [red] Você chegou ao final do livro '{self.titulo}'[/red]")

    def fimlivro(self) -> bool:
        #return True if self.paginaat == self.totalp else False | opção mais curta
        if self.paginaat == self.totalp:
            return True
        else:
            return False


l1 = Livro("Titulo bom", 20)
l1.avancar(5)
l1.avancar(10)
l1.avancar(50)
l1.avancar(5)