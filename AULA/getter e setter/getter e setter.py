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

    @classmethod
    def total_carros(cls):
          print(f"Total de carros criados pela montadora: {cls.total_carros_criados}")


    def acelerar(self, aumento):
        self.velocidade += aumento
        print(f'O automóvel acelerou para {self.velocidade} km/h.')

    def frear(self,reducao):
        self.velocidade -= reducao
        print(f'O automóvel reduziu para {self.velocidade} km/h.')


    def parar(self):
        while self.velocidade > 0:
            self.velocidade -= 5
            print(f'O automóvel está reduzindo a velocidade para {self.velocidade} km/h.')
            print('O automóvel parou.')

objeto = Montadora("Branca","flex")
#objeto.acelerar(10)
#objeto.acelerar(50)
#objeto.frear(5)
#objeto.frear(15)
#objeto.parar()

carro1 = Montadora("vermelha", "flex")
Montadora.boas_vindas()
# Ou também podemos chamar o método estático por uma instância, embora isso não seja comum.
carro1.boas_vindas()

Montadora.boas_vindas()
Montadora.total_carros()
