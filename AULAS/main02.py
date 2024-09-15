# Este arquivo depende do arquivo: 'montadora02.py'. Abra-o para ver seu conteúdo.
# O arquivo montadora02.py contém a classe 'Montadora'
# para acessar a classe 'Montadora' presente no arquivo 'montadora02.py' devemos fazer:

from montadora02 import Montadora

# Para instanciar um objeto precisamos chamar a classe e enviar 5 valores para os
# parametros da classe:

y = Montadora('vermelha',100,6,'diesel',0.0)

print(y.cor,
      y.qtdLitros,
      y.qtdPassageiros,
      y.tipoCombustivel,
      y.velocidade)


# Observe agora que vou alterar o atributo cor do objeto y:
y.cor = 'amarela'
print('Atributos de y:',y.cor,y.qtdLitros,y.qtdPassageiros,y.tipoCombustivel,y.velocidade)


# Um programa em POO não deve permitir que seus atributos sejam alterados livremente
# dentro do código. No exemplo montadora03.py vamos entender como
# encapsular atributos em python.

