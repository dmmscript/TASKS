class Montadora:

    total_carros_criados = 0

    def __init__(self, cor, tipo_de_combustivel, velocidade=0):
        self.cor = cor
        self.tipo_de_combustivel = tipo_de_combustivel
        self.velocidade = velocidade

        Montadora.total_carros_criados += 1
    @staticmethod
    def boas_vindas():
        print("Bem-vindo à Montadora!")

carro1 = Montadora("vermelha", "flex")

Montadora.boas_vindas()
# Ou também podemos chamar o método estático por uma instância, embora isso não seja comum.
carro1.boas_vindas()