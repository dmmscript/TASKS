class Motor:
    def __init__(self, tipo):
        self.tipo = tipo    

class Carro:
    def __init__(self, marca, modelo, motor):
        self.marca = marca
        self.modelo = modelo
        self.motor = motor

motor_v6 = Motor("V6")
meu_carro = Carro("Ford", "Mustang", motor_v6)


