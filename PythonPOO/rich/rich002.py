from rich import print
from rich.panel import Panel

caixa = Panel("[white]esse aqui é um painel de exemplo[/white]", title="mensagem", style="red", width=35)

print(caixa)