class Avaliacao:
    def __init__(self, nome, disciplina, nota = 0):
        self.nome = nome
        self.disciplina = disciplina
        self._nota = nota

    #criando atributo validavel
    @property 
    def nota(self): #getter
        return self._nota

    @nota.setter #setter
    def nota(self, valor):
        if  0 <= valor <= 10:
            self._nota =  valor
        else:
            print("Nota invalida!")



''' def get_nota(self): #metodo getter
        return self._nota

    def set_nota(self, valor): #metodo setter
        if  0 <= valor <= 10:
            self._nota =  valor
        else:
            print("Nota invalida!")'''
