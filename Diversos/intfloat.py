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
    try:
        ok = False
        valor = 0
        while True:
            n = str(input(msg))
            if n.isinstance(float):
                valor = float(n)
                ok = True
            if ok:
              break
            else: 
                valor == type: str
            
    except (ValueError, TypeError):
        print("porfavor digite um numero real valido")
    except (KeyboardInterrupt):
        print("o usuario preferiu nao digitar esse numero!")
        
    return valor

