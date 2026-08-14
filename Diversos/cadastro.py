alunos = []


def cadastrar_aluno():
  print("\n--- CADASTRAR ALUNO ---")
  nome = input("Digite o nome do aluno: ")
  nota1 = float(input("Digite a nota 1: "))
  nota2 = float(input("Digite a nota 2: "))

  aluno = {"nome": nome, "nota1": nota1, "nota2": nota2}
  alunos.append(aluno)
  print(f"Aluno {nome} cadastrado com sucesso!\n")


def listar_alunos():
  print("\n===== ALUNOS =====")
  if not alunos:
    print("Nenhum aluno cadastrado ainda.\n")
    return

  for i, aluno in enumerate(alunos, start=1):
    print(
        f"{i}. {aluno['nome']} - Notas: {aluno['nota1']}, {aluno['nota2']}"
    )
  print()


def calcular_media():
  print("\n--- CALCULAR MÉDIA ---")
  if not alunos:
    print("Nenhum aluno cadastrado ainda para calcular média.\n")
    return

  nome_busca = input("Digite o nome do aluno: ")
  aluno_encontrado = None

  for aluno in alunos:
    if aluno["nome"].lower() == nome_busca.lower():
      aluno_encontrado = aluno
      break

  if aluno_encontrado:
    media = (aluno_encontrado["nota1"] + aluno_encontrado["nota2"]) / 2

    if media >= 6.0:
      situacao = "Aprovado"
    else:
      situacao = "Reprovado"

    print(f"\nMédia: {media:.1f}")
    print(f"Situação: {situacao}\n")
  else:
    print(f"Aluno '{nome_busca}' não encontrado.\n")


def main():
  while True:
    print("===== SISTEMA =====")
    print("1 - Cadastrar aluno")
    print("2 - Listar alunos")
    print("3 - Calcular média")
    print("4 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
      cadastrar_aluno()
    elif opcao == "2":
      listar_alunos()
    elif opcao == "3":
      calcular_media()
    elif opcao == "4":
      print("Saindo do sistema. Até logo!")
      break
    else:
      print("Opção inválida! Escolha um número de 1 a 4.\n")


if __name__ == "__main__":
  main()