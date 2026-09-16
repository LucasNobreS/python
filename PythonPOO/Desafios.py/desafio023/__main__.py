from rich import print
from poligono import Quadrado
from poligono import Circulo

def main():
    q1 = Quadrado(12)

    print(f"Perimetro= {q1.Perimetro():.1f}: ")
    print(f"area = {q1.Area():.1f}: ")


    c1 = Circulo()

    print(f' Um circulo de raio {c1.raio} tem perimetro de {c1.Perimetro():.1f}')
    print(f'Um circulo com {c1.raio} de raio tem area de {c1.Area():.1f}')
if __name__ == "__main__":
    main()
