# Este arquivo depende do arquivo: 'arqTeste02.py'. Abra-o para ver seu conteúdo.
# O arquivo arqTeste02.py contém a classe 'Teste02'
# para acessar a classe 'Teste02' presente do arquivo 'arqTeste02.py' devemos fazer:
from montadora04 import Montadora

# Para instanciar um objeto precisamos chamar a classe e enviar 5 parâmetros para os
# argumentos da classe:

y = Montadora('vermelha',100,6,'diesel',0.0)

# print('Atributos de y:',y.__tipoCombustivel) isso não funciona
print('Atributos de y:',y.tipoCombustivel) # isso funciona

y.qtdPassageiros = 7 # isso funciona
print('Atributos de y:',y.qtdPassageiros) # isso funciona


# Agora é a sua vez de praticar. Crie uma Classe chamada 'Conta'. Essa classe deve ter os
# seguintes atributos: nomeTitular, numeroConta, saldo.
# Crie métodos que permitam alterar o saldo desta conta e imprimir os dados desta.


