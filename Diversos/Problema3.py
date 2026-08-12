senhas = ["abc", "123456", "senha123", "senha1234", "senha12345", "senha123456", "oi"]

for senha in senhas:
    if len(senha) >= 6:
        print(f"A senha {senha} é valida!")
    else:
        print(f"A senha {senha} é invalida e deve ter pelo menos 6 caracteres!")