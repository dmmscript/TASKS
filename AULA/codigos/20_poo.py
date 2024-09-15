from abc import ABC, abstractmethod
import math

# Classe abstrata base
class Forma(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def cor(self):
        pass

# Classe concreta para Retângulo
class Retangulo(Forma):
    def __init__(self, largura, altura, cor):
        self.largura = largura
        self.altura = altura
        self.__cor = cor  # Propriedade privada para a cor

    def area(self):
        return self.largura * self.altura

    def cor(self):
        return self.__cor

# Classe concreta para Círculo
class Circulo(Forma):
    def __init__(self, raio, cor):
        self.raio = raio
        self.__cor = cor  # Propriedade privada para a cor

    def area(self):
        return math.pi * (self.raio ** 2)

    def cor(self):
        return self.__cor

# Criação de instâncias das classes
ret = Retangulo(5, 10, "vermelho")
cir = Circulo(7, "azul")

# Impressão da área e cor de cada forma
print(f"Área do Retângulo: {ret.area()}")  # Output: 50
print(f"Cor do Retângulo: {ret.cor()}")    # Output: vermelho
print(f"Área do Círculo: {cir.area():.2f}") # Output: 153.94 (aproximadamente)
print(f"Cor do Círculo: {cir.cor()}")      # Output: azul

