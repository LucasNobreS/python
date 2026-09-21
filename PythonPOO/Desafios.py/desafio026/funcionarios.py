from abc import ABC, abstractmethod
from rich.panel import Panel
from rich import print

class Funcionario(ABC):
    def __init__(self, nome, sal_bruto=0, salario=0, sal_min=1620, inss=0.075):
        self.nome = nome
        self.sal_bruto = sal_bruto
        self.salario = salario
        self.sal_min = sal_min
        self.inss = inss

    @abstractmethod
    def calc_sal(self):
        pass

class FuncHorista(Funcionario):
    def __init__(self, nome, horastrab, valhora, inss=0.075, sal_min= 1620 ):
        super().__init__(nome=nome, inss=inss, sal_min=sal_min)
        self.horastrab = horastrab
        self.valhora = valhora

    def calc_sal(self):
        result = (self.horastrab * self.valhora) 
        saldo = result - (result * self.inss)
        print(saldo)
        return saldo

    def analisar(self):
        qtde = self.calc_sal()/ self.sal_min
        print( Panel(f"O salário de [blue]{self.nome}[/blue] ([yellow]{__class__.__name__}[/yellow]) é de [green]R${self.calc_sal():.2f}[/green], e corresponde a [red]{qtde:.2f}[/red] salários mínimos" ,title="Calculando Salário",  width=60))


class FuncMensal(Funcionario):
    def __init__(self, nome, sal_bruto=0, salario=0, sal_min=1620, inss=0.075):
        super().__init__(nome, sal_bruto, salario, sal_min, inss)

    def calc_sal(self):
        saldo = self.sal_bruto - (self.sal_bruto * self.inss)
        return saldo

    def analisar(self):
        qtde = self.calc_sal()/ self.sal_min
        print( Panel(f"O salário de [blue]{self.nome}[/blue] ([yellow]{__class__.__name__}[/yellow]) é de [green]R${self.calc_sal():.2f}[/green], e corresponde a [red]{qtde:.2f}[/red] salários mínimos" ,title="Calculando Salário",  width=60))