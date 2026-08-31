from rich import inspect
from aluno import Aluno
from professor import Professor
from funcionario import Funcionario



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