from funcionarios import *


def main():
    f1 = FuncHorista(str(input("Nome do funcionário: ")), float(input("Horas trabalhadas: ")), float(input("Valor da hora: ")))
    f2 = FuncMensal(str(input("Nome do funcionário: ")), float(input("Salário bruto: ")))
    
    f1.calc_sal()
    f1.analisar()
    f2.calc_sal()
    f2.analisar()


if __name__ == "__main__":
    main()