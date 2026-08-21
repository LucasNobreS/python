def leiaint(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mERRO!, digite um numero inteiro valido!\033[m')
        if ok:
            break
    return valor

def leiafloat(msg):
    while True:
        try:
            valor = float(input(msg))
            return valor
        except (ValueError, TypeError):
            print("porfavor digite um numero real valido")
        except KeyboardInterrupt:
            print("o usuario preferiu nao digitar esse numero!")
            return 0


