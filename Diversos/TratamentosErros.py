#print(x) #excessão
try:
    a = int(input('Numerador:'))
    b = int(input("Denominador: "))

    r = a/b
except (ValueError, TypeError):
    print('tivemos um problema com o tipo de dados que voce digitou.')
except ZeroDivisionError:
    print('Não é possivel dividir por 0')
except KeyboardInterrupt:
    print('o usuario decidiu nao informar os dados')
else:
    print(f'O resultado é: {r}')
finally:
    print('Volte  sempre obrigado!')

