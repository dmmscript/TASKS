class Montadora:
    def __init__(self,p1,p2,p3):
        self.cor= p1
        self.velocidade= p2
        self.tipo_combustivel= p3

objeto_1 = Montadora('branca',0.0,'flex')
objeto_2 = Montadora('preta',0.0,'diesel')

print('Atributos de objeto_1:',objeto_1.cor, objeto_1.tipo_combustivel, objeto_1.velocidade)
print('Atributos de objeto_2:',objeto_2.cor, objeto_2.tipo_combustivel, objeto_2.velocidade)