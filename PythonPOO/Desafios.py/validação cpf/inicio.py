from validacpf import valida_cpf
from gerar import gerar_cpf

escolha = 3
while escolha > 0:
    escolha = int(input("ESCOLHA UMA OPÇÃO:\n 1-Validar cpf \n 2-Gerar cpf valido \n 0-SAIR\n"))
    
    if escolha == 0:
        break
    elif escolha == 1:
        valida_cpf(cpf = str(input("Digite o CPF(no formato 123456789-10): ")).replace("-","").replace(".",""))
    elif escolha == 2:
        print(gerar_cpf())
    else:
        print("opcao invalida!")
