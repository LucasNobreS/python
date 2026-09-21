from abc import ABC, abstractmethod


class Transporte(ABC):
    def __init__(self, distancia):
        self.distancia = distancia

    @abstractmethod
    def calc_frete(self):
        pass

class Moto(Transporte):
    def __init__(self, distancia):
        super().__init__(distancia)
        

    def calc_frete(self):
        return self.distancia * 0.5

class Caminhao(Transporte):
    def __init__(self, distancia):
            super().__init__(distancia)
            

    def calc_frete(self):
        if self.distancia > 50:
             return self.distancia * 1.20
        else:
             return " frete de caminhão tem a distancia minima é 50km"


class Drone(Transporte):
    def __init__(self, distancia):
            super().__init__(distancia)
            
    
    def calc_frete(self):
        if self.distancia > 50:
            return self.distancia * 9.5
        else:
            return " frete de drona tem a distancia maxima é 10km"