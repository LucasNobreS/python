from rich import inspect

class Pessoa:
    def __init__(self, nome = "", idade= 0):
        self.nome = nome
        self.idade = idade

    def Aniversario(self):
        self.idade +=1


class Aluno(Pessoa):
    def __init__(self, nome, idade, curso, turma):
        super().__init__(nome, idade)
        self.curso = curso
        self.turma = turma
    def Matricula(self):
        print(f'O aluno {self.nome} acabou de fazer matricula')


class Professor(Pessoa):
    def __init__(self, nome, idade, especialidade, nivel):
        super().__init__(nome, idade)
        self.especialidade= especialidade
        self.nivel = nivel
    def Aula(self):
        print(f'O professor {self.nome} começou a dar aula')


class Funcionario(Pessoa):
    def __init__(self, nome, idade, cargo, setor):
        super().__init__(nome, idade)
        self.cargo = cargo
        self.setor =setor
    def Ponto(self):
        print(f'O funcionario {self.nome} acabou de bater o ponto')


a1 = Aluno("José", 17, "Informatica", "T01")
a1.Aniversario()
a1.Matricula()
inspect(a1)

p1 = Professor("Samuel", 37, "Biologia", "Mestre")
p1.Aniversario()
p1.Aula()
inspect(p1)

f1 = Funcionario("Claudia",27, "Secretária", "Secretaria")
f1.Aniversario()
f1.Ponto()
inspect(f1)