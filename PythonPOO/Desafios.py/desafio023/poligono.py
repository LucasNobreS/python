from abc import ABC, abstractmethod
import math


class Poligono(ABC):
    def __init__(self, lados):
        self.lados = lados

    @abstractmethod
    def Perimetro(self) -> float:
        pass

    @abstractmethod
    def Area(self) -> float:
        pass

class Quadrado(Poligono):

    def __init__(self, lados = 1):
        super().__init__(4)
        self.lados = lados

    def Perimetro(self):
            return self.lados * 4

    def Area(self):
            return self.lados ** 2

class Circulo(Poligono):

    def __init__(self, raio = 1):
        super().__init__(0)
        self.raio = raio

    def Perimetro(self):
                return 2 * math.pi * self.raio
    
    def Area(self):
                return math.pi * self.raio ** 2