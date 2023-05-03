class Animal:
    def andar(self):
        print("Estou andando")

    def correr(self):
        print("Estou correndo")

    def pular(self):
        print("Estou pulando")

class Felino(Animal):
    def felino(self):
        print('eu sou um felino')

class Gato(Animal):
    def miar(self):
        print("Estou miando")

class Cachorro(Animal):
    def latir(self):
        print("esotu latindo")

g1 = Gato()
g1.andar()

c1 = Cachorro()
c1.andar()