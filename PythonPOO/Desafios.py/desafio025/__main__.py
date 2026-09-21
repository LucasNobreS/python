from veiculos import *

def main():
    distancia = 20
    v1 = Caminhao(distancia)
    print(f' um frete de {v1.__class__.__name__} com a distancia {distancia}km: {v1.calc_frete()}')

if __name__ == "__main__":
    main()