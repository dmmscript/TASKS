class Montadora:
    cor=''
    velocidade=''
    tipo_combustivel=''

objeto_1 = Montadora()
objeto_2 = Montadora()

objeto_1.cor = 'preta'
objeto_1.tipo_combustivel='flex'
objeto_1.velocidade=0.0

objeto_2.cor = 'branca'
objeto_2.tipo_combustivel='diesel'
objeto_2.velocidade=0.0

print('Atributos de objeto_1:',objeto_1.cor, objeto_1.tipo_combustivel, objeto_1.velocidade)
print('Atributos de objeto_2:',objeto_2.cor, objeto_2.tipo_combustivel, objeto_2.velocidade)