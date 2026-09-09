"""Banco simples com Python"""

from rich import print
from rich.panel import Panel


contas = []


class Conta:

    def __init__(self, nome, numero, senha, saldo=0):
        self.nome = nome
        self.numero = numero
        self.senha = senha
        self.saldo = saldo

    def cadastrar(self):
        contas.append(self)

        print(
            Panel(
                f"[bold green]CONTA CADASTRADA COM SUCESSO![/bold green]\n\n"
                f"[bold]Nome:[/bold] {self.nome}\n"
                f"[bold]Número da conta:[/bold] {self.numero}\n"
                f"[bold]Saldo inicial:[/bold] R$ {self.saldo:.2f}",
                title="[bold cyan]🏦 Banco Python[/bold cyan]",
                border_style="green"
            )
        )

    def deposito(self):

        valor = float(input("Digite o valor que deseja depositar: R$ "))

        if valor > 0:

            self.saldo += valor

            print(
                Panel(
                    f"[bold green]DEPÓSITO REALIZADO![/bold green]\n\n"
                    f"Valor depositado: R$ {valor:.2f}\n"
                    f"Saldo atual: R$ {self.saldo:.2f}",
                    title="[bold cyan]💰 Depósito[/bold cyan]",
                    border_style="green"
                )
            )

        else:
            print(
                Panel(
                    "[bold red]O valor precisa ser maior que zero![/bold red]",
                    title="[bold red]Erro[/bold red]",
                    border_style="red"
                )
            )

    def saque(self):

        valor = float(input("Digite o valor que deseja sacar: R$ "))

        if valor <= 0:

            print(
                Panel(
                    "[bold red]O valor precisa ser maior que zero![/bold red]",
                    title="[bold red]Erro[/bold red]",
                    border_style="red"
                )
            )

        elif valor > self.saldo:

            print(
                Panel(
                    f"[bold red]SALDO INSUFICIENTE![/bold red]\n\n"
                    f"Saldo disponível: R$ {self.saldo:.2f}",
                    title="[bold red]Saque[/bold red]",
                    border_style="red"
                )
            )

        else:

            self.saldo -= valor

            print(
                Panel(
                    f"[bold green]SAQUE REALIZADO![/bold green]\n\n"
                    f"Valor sacado: R$ {valor:.2f}\n"
                    f"Saldo atual: R$ {self.saldo:.2f}",
                    title="[bold cyan]💸 Saque[/bold cyan]",
                    border_style="green"
                )
            )

    def consultar_saldo(self):

        print(
            Panel(
                f"[bold]Titular:[/bold] {self.nome}\n"
                f"[bold]Conta:[/bold] {self.numero}\n\n"
                f"[bold green]Saldo:[/bold] R$ {self.saldo:.2f}",
                title="[bold cyan]💳 Saldo da Conta[/bold cyan]",
                border_style="cyan"
            )
        )


def acessar():

    numero_digitado = input("Digite o número da conta: ")

    for conta_atual in contas:

        if conta_atual.numero == numero_digitado:

            print(
                Panel(
                    "[bold green]Conta encontrada![/bold green]",
                    border_style="green"
                )
            )

            senha_digitada = input("Digite sua senha: ")

            if conta_atual.senha == senha_digitada:

                print(
                    Panel(
                        f"[bold green]ACESSO AUTORIZADO![/bold green]\n\n"
                        f"Bem-vindo, [bold cyan]{conta_atual.nome}[/bold cyan]!",
                        title="[bold cyan]🔐 Login[/bold cyan]",
                        border_style="cyan"
                    )
                )

                return conta_atual

            else:

                print(
                    Panel(
                        "[bold red]Senha incorreta![/bold red]",
                        title="[bold red]Acesso negado[/bold red]",
                        border_style="red"
                    )
                )

                return None

    print(
        Panel(
            "[bold red]Nenhuma conta foi encontrada com esse número.[/bold red]",
            title="[bold red]Acesso negado[/bold red]",
            border_style="red"
        )
    )

    return None


# ==========================================
# PROGRAMA PRINCIPAL
# ==========================================

opcao = ""

while opcao != "0":

    print(
        Panel(
            "[bold cyan]1[/bold cyan] - Acessar conta\n"
            "[bold cyan]2[/bold cyan] - Cadastrar conta\n"
            "[bold cyan]0[/bold cyan] - Sair",
            title="[bold cyan]🏦 BANCO PYTHON[/bold cyan]",
            subtitle="Sistema bancário",
            border_style="cyan"
        )
    )

    opcao = input("Selecione uma opção: ")

    # ======================================
    # ACESSAR CONTA
    # ======================================

    if opcao == "1":

        conta_logada = acessar()

        if conta_logada:

            while True:

                print(
                    Panel(
                        f"[bold]Titular:[/bold] {conta_logada.nome}\n"
                        f"[bold]Conta:[/bold] {conta_logada.numero}\n"
                        f"[bold green]Saldo:[/bold green] R$ {conta_logada.saldo:.2f}\n\n"
                        "[bold cyan]1[/bold cyan] - Depósito\n"
                        "[bold cyan]2[/bold cyan] - Saque\n"
                        "[bold cyan]3[/bold cyan] - Consultar saldo\n"
                        "[bold cyan]0[/bold cyan] - Sair da conta",
                        title="[bold cyan]💳 ÁREA DA CONTA[/bold cyan]",
                        border_style="cyan"
                    )
                )

                escolha = input("Selecione uma opção: ")

                if escolha == "1":

                    conta_logada.deposito()

                elif escolha == "2":

                    conta_logada.saque()

                elif escolha == "3":

                    conta_logada.consultar_saldo()

                elif escolha == "0":

                    print(
                        Panel(
                            "[bold yellow]Você saiu da conta.[/bold yellow]",
                            border_style="yellow"
                        )
                    )

                    break

                else:

                    print(
                        Panel(
                            "[bold red]Opção inválida![/bold red]",
                            border_style="red"
                        )
                    )

    # ======================================
    # CADASTRAR CONTA
    # ======================================

    elif opcao == "2":

        nome = input("Digite seu nome: ")
        numero = input("Digite o número da conta: ")
        senha = input("Digite sua senha: ")

        nova_conta = Conta(nome, numero, senha)

        nova_conta.cadastrar()

    # ======================================
    # SAIR
    # ======================================

    elif opcao == "0":

        print(
            Panel(
                "[bold cyan]Obrigado por utilizar o Banco Python![/bold cyan]\n"
                "Até logo!",
                title="[bold]🏦 BANCO PYTHON[/bold]",
                border_style="cyan"
            )
        )

    else:

        print(
            Panel(
                "[bold red]Opção inválida![/bold red]\n"
                "Escolha uma das opções disponíveis.",
                title="[bold red]Erro[/bold red]",
                border_style="red"
            )
        )