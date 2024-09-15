class Montadora:

    total_carros_criados = 0

    def __init__(self, cor, tipo_de_combustivel, velocidade=0):
        self.cor = cor
        self.tipo_de_combustivel = tipo_de_combustivel
        self.velocidade = velocidade

        Montadora.total_carros_criados += 1

    @classmethod
    def total_carros(cls):
        print(f"Total de carros criados pela montadora: {cls.total_carros_criados}"
)

carro1 = Montadora("vermelha", "flex")

Montadora.total_carros()
carro1.total_carros() # Não faça desta forma