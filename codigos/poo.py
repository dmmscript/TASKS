class Montadora:
    def __init__(self,p1,p2,p3,p4,p5): # metodo construtor
        self.cor = p1
        self.qtdPassageiros = p2
        self.tipoCombustivel = p3
        self.velocidade = p4
        self.litros = p5

objeto_1 = Montadora("branca",5,"flex",160,42) # estou instanciando um objeto!
objeto_2 = Montadora("preta",6,"diesel",200,60) # quando vc instancia um objet, o metodo construtor da classe é chamado, caso exista.


print(objeto_1.cor, objeto_2.litros)