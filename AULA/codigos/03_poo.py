class Montadora:
    def __init__(self, cor, tipo_de_combustivel, velocidade=0):
        self.cor = cor
        self.tipo_de_combustivel = tipo_de_combustivel
        self.velocidade = velocidade

    def acelerar(self, aumento):
        self.velocidade += aumento
        print(f'O automóvel acelerou para {self.velocidade} km/h.')

    def frear(self,reducao):
        self.velocidade -= reducao
        print(f'O automóvel reduziu para {self.velocidade} km/h.')

    def parar(self):
        self.velocidade = 0
        print('O automóvel parou.')

objeto = Montadora("Branca","flex")
objeto.acelerar(10)
objeto.acelerar(20)
objeto.frear(5)
objeto.frear(15)
objeto.parar()