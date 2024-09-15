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
            print(f'Depósito de R${valor:.2f} realizado com sucesso para {self.titular}.')
        else:
            print('O valor do depósito deve ser positivo.')

    def sacar(self, valor):
        if valor > 0:
            if valor <= self.__saldo:
                self.__saldo -= valor
                print(f'Saque de R${valor:.2f} realizado com sucesso para {self.titular}.')
            else:
                print('Saldo insuficiente para realizar o saque.')
        else:
            print('O valor do saque deve ser positivo.')

    def consultar_saldo(self):
        print(f'Saldo atual de {self.titular}: R${self.__saldo:.2f}')

class Banco:
    def __init__(self):
        self.contas = []

    def adicionar_conta(self, conta):
        self.contas.append(conta)
        print(f'Conta de {conta.titular} adicionada com sucesso.')

    def remover_conta(self, titular):
        for conta in self.contas:
            if conta.titular == titular:
                self.contas.remove(conta)
                print(f'Conta de {titular} removida com sucesso.')
                return
        print(f'Conta de {titular} não encontrada.')

    def listar_contas(self):
        print('Listando todas as contas no banco:')
        for conta in self.contas:
            print(f'- {conta.titular}, Saldo: R${conta.saldo:.2f}')

    def operar_conta(self, titular):
        for conta in self.contas:
            if conta.titular == titular:
                return conta
        print(f'Conta de {titular} não encontrada.')
        return None


# Exemplo de uso das classes Banco e ContaBancaria
banco = Banco()

# Criando contas bancárias
conta1 = ContaBancaria('João Bosco', 1000)
conta2 = ContaBancaria('Ana Maria', 500)

# Adicionando contas ao banco
banco.adicionar_conta(conta1)
banco.adicionar_conta(conta2)

# Listando contas no banco
banco.listar_contas()

# Operando em uma conta específica
conta_operar = banco.operar_conta('João Bosco')
if conta_operar:
    conta_operar.consultar_saldo()
    conta_operar.depositar(300)
    conta_operar.sacar(100)
    conta_operar.consultar_saldo()

# Removendo uma conta
banco.remover_conta('Ana Maria')

# Listando contas no banco após remoção
banco.listar_contas()
