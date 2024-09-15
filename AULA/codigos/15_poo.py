class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def info(self):
        return f'{self.marca} {self.modelo}'

class Carro(Veiculo):
    def __init__(self, marca, modelo, num_portas):
        super().__init__(marca, modelo)
        self.num_portas = num_portas

    def info(self):
        return f'{self.marca} {self.modelo}, {self.num_portas} portas'

meu_carro = Carro('Toyota', 'Corolla', 4)
print(meu_carro.info())  # Output: Toyota Corolla, 4 portas
