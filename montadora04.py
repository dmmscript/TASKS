
# O acesso aos atributos encapsulados deve ser feito por meio dos métodos getters/setters.
# Esses métodos permitem ler/escrever valores dos/nos atributos encapsulados.


class Montadora:
    def __init__(self, cor, velocidade, qtdPassageiros, tipoCombustivel, qtdLitros):
        self.__cor=cor
        self.__velocidade=velocidade
        self.__qtdPassageiros=qtdPassageiros
        self.__tipoCombustivel=tipoCombustivel
        self.__qtdLitros=qtdLitros

    # Getter para cor ============================================
    @property
    def cor(self):
        return self.__cor

    # Setter para cor__cor
    @cor.setter
    def cor(self, novo_cor):
        if isinstance(novo_cor, str) and novo_cor.strip():
            self.__cor = novo_cor
        else:
            raise ValueError("cor deve ser uma string não vazia.")
        
    # Getter para velocidade =====================================
    @property
    def velocidade(self):
        return self.__velocidade

    # Setter para velocidade
    @velocidade.setter
    def velocidade(self, nova_velocidade: float):
        if isinstance(nova_velocidade, float) and nova_velocidade >= 0:
            self.__velocidade = nova_velocidade
        else:
            raise ValueError("Velocidade deve ser um número float não negativo.")

    # Getter para qtdPassageiros ==================================
    @property
    def qtdPassageiros(self):
        return self.__qtdPassageiros

    # Setter para qtdPassageiros
    @qtdPassageiros.setter
    def qtdPassageiros(self, nova_qtd: int):
        if isinstance(nova_qtd, int) and nova_qtd >= 0:
            self.__qtdPassageiros = nova_qtd
        else:
            raise ValueError("Quantidade de passageiros deve ser um número inteiro não negativo.")


    # Getter para tipoCombustivel ============================================
    @property
    def tipoCombustivel(self):
        return self.__tipoCombustivel

    # Setter para nome
    @tipoCombustivel.setter
    def tipoCombustivel(self, novo_tipoCombustivel):
        if isinstance(novo_tipoCombustivel, str) and novo_tipoCombustivel.strip():
            self.__tipoCombustivel = novo_tipoCombustivel
        else:
            raise ValueError("Tipo combustivel deve ser uma string não vazia.")
        

    # Getter para qtdLitros =====================================
    @property
    def qtdLitros(self):
        return self.__qtdLitros

    # Setter para qtdLitros
    @qtdLitros.setter
    def qtdLitros(self, nova_qtdLitros: float):
        if isinstance(nova_qtdLitros, float) and nova_qtdLitros >= 0:
            self.__qtdLitros = nova_qtdLitros
        else:
            raise ValueError("qtdLitros deve ser um número float não negativo.")
        
# Vamos agora para o arquivo 'main04.py' instanciar alguns objetos.
