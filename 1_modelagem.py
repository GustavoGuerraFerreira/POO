class Pessoas():
    #Atributos Classe:
    olho = True
    boca = True
    raca = "Ser Humano"
    #Método construtor
    def __init__(self, nome, idade, cpf):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
    #Método:
    def retorna_nome(self):
        return self.nome
    def logar_sistema(self):
        print(f"{self.retorna_nome()} está logando no sistema") 
    #Método Da Classe:
    @classmethod
    def andar(cls):
        cls.pernas = 2
        return None
    @staticmethod
    def adulto(idade):
        if idade > 18:
            return True
        return False
#instaciar objetos:
p1 = Pessoas('Gustavo', 20 , '14914501775')
p2 = Pessoas('Marcos', 22, '174174828299')
#acessar Atributos:
print(p1.nome)
print(p2.nome)
#acessar Métodos:
p1.logar_sistema()
p2.logar_sistema()
#acessar Atributos da Classe:
print(Pessoas.olho, Pessoas.boca, Pessoas.raca)
Pessoas.andar()
print(Pessoas.pernas)
print(Pessoas.adulto(20))