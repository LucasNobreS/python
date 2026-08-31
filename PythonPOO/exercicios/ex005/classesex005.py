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
        print(f' {self.nome} acabou de fazer matricula')


class Professor(Pessoa):
    def __init__(self, nome, idade, especialidade, nivel):
        super().__init__(nome, idade)
        self.especialidade= especialidade
        self.nivel = nivel
    def Aula(self):
        print(f' {self.nome} começou a dar aula')


class Funcionario(Pessoa):
    def __init__(self, nome, idade, cargo, setor):
        super().__init__(nome, idade)
        self.cargo = cargo
        self.setor =setor
    def Ponto(self):
        print(f'{self.nome} acabou de bater o ponto')