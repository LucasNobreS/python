class ContaBancaria:
    """
    cria uma conta bancaria e permite fazer saques e depositos
    """

    def __init__(self, id, nome, saldo = 0):
        self.id = id
        self.titular = nome
        self.saldo = saldo
        print(f"Conta {self.id} criada com sucesso, saldo atual de R${self.saldo:,.2f}")

    def __str__(self):
        return f"a conta {self.id} de {self.titular} tem R${self.saldo:,.2f}"

    def depositar(self, valor):
        self.saldo += valor
        print(f"Deposito de R${valor: ,.2f} na conta {self.id}")

    def sacar(self, valor):
        if valor > self.saldo:
            print(f"saque NEGADO de R${valor:,.2f} na conta {self.id}, saldo insuficiente")
        else:
            self.saldo-=valor
            print(f"Saque de R${valor:,.2f} autorizado na conta {self.id}")





c1 = ContaBancaria(112, "Lucas", 3000)
c1.depositar(500)
c1.sacar(1500)
c1.sacar(2000000)
print(c1)


