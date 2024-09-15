class ContaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.__saldo = saldo_inicial

    @property
    def saldo(self):
        return self.__saldo

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            print(f'Depósito de R${valor:.2f} realizado com sucesso.')
        else:
            print('O valor do depósito deve ser positivo.')

    def sacar(self, valor):
        if valor > 0:
            if valor <= self.__saldo:
                self.__saldo -= valor
                print(f'Saque de R${valor:.2f} realizado com sucesso.')
            else:
                print('Saldo insuficiente para realizar o saque.')
        else:
            print('O valor do saque deve ser positivo.')

    def consultar_saldo(self):
        print(f'Saldo atual: R${self.__saldo:.2f}')

# Exemplo de uso da classe ContaBancaria
conta = ContaBancaria('João Silva', 1000)
conta.consultar_saldo() # Exibe o saldo inicial
conta.depositar(500)# Realiza um depósito
conta.sacar(200) # Realiza um saque
conta.consultar_saldo() # Exibe o saldo após as transações
conta.sacar(1500) # Tenta sacar mais do que o saldo disponível