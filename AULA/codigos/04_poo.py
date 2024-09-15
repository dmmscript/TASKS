class Montadora:

    total_carros_criados = 0

    def __init__(self, cor, tipo_de_combustivel, velocidade=0):
        self.cor = cor
        self.tipo_de_combustivel = tipo_de_combustivel
        self.velocidade = velocidade

        Montadora.total_carros_criados += 1

    def acelerar(self, aumento):
        self.velocidade += aumento
        print(f'O automóvel acelerou para {self.velocidade} km/h.')

    def frear(self,reducao):
        self.velocidade -= reducao
        print(f'O automóvel reduziu para {self.velocidade} km/h.')

    def parar(self):
        self.velocidade = 0
        print('O automóvel parou.')


carro1 = Montadora("vermelha", "flex")
carro2 = Montadora("branca", "diesel")
carro3 = Montadora("preta", "eletricidade")
print(f"Total: {Montadora.total_carros_criados} Total:{carro1.total_carros_criados} ")