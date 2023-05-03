class Pessoa: 
    def falar(self):
        print('Estou falando')

    def andar(self):
        print('Estou andando')

class Vendedor(Pessoa):
    
    def vender(self):
        print('Estou vendendo')

class Cliente(Pessoa):
    def comprar(self):
        print('estou comprando')

c1 = Cliente()
c1.andar()
c1.comprar()
v1 = Vendedor()
v1.andar()
v1.vender()