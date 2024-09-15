# Neste exemplo vamos trabalhar com o 'Método Construtor'.
# Construtores servem para inicializar/construir os Objetos com valores pré-definidos na instância.
# Todos os Métodos começam com a palavra 'def'
# Um método Construtor deve ter o seguinte nome: '__init__'

class Montadora:
    def __init__(self, cor, velocidade, qtdPassageiros, tipoCombustivel, qtdLitros):
        self.cor=cor
        self.velocidade=velocidade
        self.qtdPassageiros=qtdPassageiros
        self.tipoCombustivel=tipoCombustivel
        self.qtdLitros=qtdLitros

# Vamos agora para o arquivo 'main02.py' instanciar alguns objetos.
