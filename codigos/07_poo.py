class Montadora:
    def __init__(self, cor, tipo_de_combustivel, velocidade=0):
        self.cor = cor
        self.tipo_de_combustivel = tipo_de_combustivel
        self.__velocidade = velocidade

    @property
    def velocidade(self):
        return self.__velocidade

    @velocidade.setter
    def velocidade(self, nova_velocidade):
        print("Setter sendo executado!")
        if nova_velocidade < 0:
            print("A velocidade não pode ser negativa.")
        else:
            self.__velocidade = nova_velocidade

    def acelerar(self, aumento):
        self.velocidade += aumento
        print(f'O automóvel acelerou para {self.velocidade} km/h.')

    def frear(self,reducao):
        self.velocidade -= reducao
        print(f'O automóvel reduziu para {self.velocidade} km/h.')

    def parar(self):
        self.velocidade = 0
        print('O automóvel parou.')

carro =Montadora(cor="vermelho", tipo_de_combustivel="gasolina", velocidade=0)
carro.acelerar(20) # Acelera por meio do método, o setter é chamado! 
print(f'Velocidade atual: {carro.velocidade} km/h')
carro.velocidade = 50 # Acessa diretamente, o setter é chamado! 
print(f'Velocidade atual: {carro.velocidade} km/h')
carro.frear(5) # Freia por meio do método, o setter é chamado!
print(f'Velocidade atual: {carro.velocidade} km/h')