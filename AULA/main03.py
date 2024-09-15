# Este arquivo depende do arquivo: 'montadora03.py'. Abra-o para ver seu conteúdo.
# O arquivo montadora03.py contém a classe 'Montadora'
# para acessar a classe 'Teste02' presente do arquivo 'arqTeste02.py' devemos fazer:
# from montadora03 import Montadora
class Montadora:
    def __init__(self, cor, velocidade, qtdPassageiros, tipoCombustivel, qtdLitros):
        self.__cor=cor
        self.__velocidade=velocidade
        self.__qtdPassageiros=qtdPassageiros
        self.__tipoCombustivel=tipoCombustivel
        self.__qtdLitros=qtdLitros
# Para instanciar um objeto precisamos chamar a classe e enviar 5 valores para os
# parametros da classe:

y = Montadora('azul',100,6,'diesel',0.0)


print('Atributos de y:',y.__cor,y.__qtdLitros,y.__qtdPassageiros,y.__tipoCombustivel,y.__velocidade)


# Observe que agora temos um erro. Os atributos nao podem ser acessados diretamente.
# Como resolver isso?
# R.: Com os métodos getters/setters. Abra os arquivos main04.py e arqTeste04.py


