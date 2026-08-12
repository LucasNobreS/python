A = input("informe um valor para variavel A: ")
B = input("informe um valor para variavel B: ")

if (A>B):
    aux=A;
    A=B;
    B=aux;
print("O valor de A agora  é: ", A)
print("O valor de B agora  é: ", B)