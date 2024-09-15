class Animal:
    def fazer_som(self):
        pass

class Cachorro(Animal):
    def fazer_som(self):
        return "Latido"

class Gato(Animal):
    def fazer_som(self):
        return "Miau"

animais = [Cachorro(), Gato()]
for animal in animais:
    print(animal.fazer_som())