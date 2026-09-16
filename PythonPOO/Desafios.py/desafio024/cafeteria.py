from abc import ABC, abstractmethod

class BebidaQuente(ABC):

    def preparar(self):
        print("----preparando bebida----")
        self.ferver()
        self.misturar()
        self.servir()
        print("----bebida pronta----\n\n\n")

    def ferver(self):
        print("1. Fervendo a 100 graus celsius.")


    @abstractmethod
    def misturar(self):
        pass


    @abstractmethod
    def servir(self):
        pass

class Cafe(BebidaQuente):
    def servir(self):
        print("3. Servindo em xicará pequena")


    def misturar(self):
        print("2. Passando a agua quente pelo pó de café")

class Cha(BebidaQuente):
    def servir(self):
        print("3.Servindo na caneca de porcelana com limão")

    def misturar(self):
        print("2.Mergulhando o sachê na agua quente.")

class Leite(BebidaQuente):
    def servir(self):
        print("3.Servindo na caneca grande já com o café.")


    def misturar(self):
        print("2.Passando pelo bico do leite")