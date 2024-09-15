class ContaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.__saldo = saldo_inicial

    @property
    def saldo(self):
        """Retorna o saldo da conta."""
        return self.__saldo

    @saldo.setter
    def saldo(self, novo_saldo):
        """Define um novo saldo para a conta, com validação."""
        if novo_saldo >= 0:
            self.__saldo = novo_saldo
            print(f'Saldo atualizado para R${novo_saldo:.2f}.')
        else:
            print('O saldo não pode ser negativo.')

    def depositar(self, valor):
        """Deposita um valor na conta, se for positivo."""
        if valor > 0:
            self.__saldo += valor
            print(f'Depósito de R${valor:.2f} realizado com sucesso.')
        else:
            print('O valor do depósito deve ser positivo.')

    def sacar(self, valor):
        """Saca um valor da conta, se houver saldo suficiente e o valor for positivo."""
        if valor > 0:
            if valor <= self.__saldo:
                self.__saldo -= valor
                print(f'Saque de R${valor:.2f} realizado com sucesso.')
            else:
                print('Saldo insuficiente para realizar o saque.')
        else:
            print('O valor do saque deve ser positivo.')

    def consultar_saldo(self):
        """Consulta o saldo atual da conta."""
        print(f'Saldo atual: R${self.__saldo:.2f}')


# Exemplo de uso da classe ContaBancaria
conta = ContaBancaria('João Silva', 1000)
conta.consultar_saldo()  # Exibe o saldo inicial

# Operações válidas usando métodos de instância
conta.depositar(500)     # Realiza um depósito
conta.sacar(200)         # Realiza um saque
conta.consultar_saldo()  # Exibe o saldo após as transações

# Uso indevido do setter para modificar diretamente o saldo
conta.saldo = 2000       # Ajusta diretamente o saldo para um valor arbitrário
conta.consultar_saldo()  # Exibe o novo saldo, sem transação válida

# Outro uso indevido do setter para definir um saldo negativo
conta.saldo = -100       # Tenta ajustar o saldo para um valor negativo
conta.consultar_saldo()  # Exibe o saldo após a tentativa de ajuste
