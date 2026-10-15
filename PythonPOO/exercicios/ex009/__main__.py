from ex009 import *
from rich import print, inspect

def main():
    av1 = Avaliacao("pedro", "matematica", 9.5)
    av1.set_nota(10)
    inspect(av1, private= True)








if __name__ == "__main__":
    main()
