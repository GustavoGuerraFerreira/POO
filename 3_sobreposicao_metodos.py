class Pessoa: 

    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf
    def falar(self):
        print('Estou falando')

    def andar(self):
        print('Estou andando')

class Cliente(Pessoa):
    def __init__(self, id_cliente, nome , cpf):
        super().__init__(nome, cpf)
        self.id_cliente = id_cliente

        
    def comprar(self):
        print('estou comprando')

    def falar(self):
        print('Estou gritando')
class Vendedor(Pessoa):
    def __init__(self, id_vendedor, nome, cpf):
        super().__init__(nome, cpf)
        self.id_vendedor = id_vendedor


c1 = Cliente(2, "Gustavo Guerra", 23131232)
c1.comprar()
c1.falar()
v1 = Vendedor(22, 'Maria', 321312312)

print(v1.nome)
print(c1.nome)