class Funcionario:
    def __init__(self, nome, cargo, salario):
        self.nome = nome
        self.cargo = cargo
        self.__salario = salario

    @property
    def salario(self):
        return self.__salario

    @salario.setter
    def salario(self, novo_salario):
        if novo_salario > 0:
            self.__salario = novo_salario
            print(f'Salário atualizado para R${novo_salario:.2f}.')
        else:
            print('O salário deve ser um valor positivo.')

    def promover(self, novo_cargo):
        self.cargo = novo_cargo
        print(f'Cargo atualizado para {novo_cargo}.')

    def exibir_informacoes(self):
        print(f'Nome: {self.nome}')
        print(f'Cargo: {self.cargo}')
        print(f'Salário: R${self.__salario:.2f}')

# Exemplo de uso da classe Funcionario
funcionario = Funcionario('Ana Costa', 'Analista', 4000)
funcionario.exibir_informacoes()
funcionario.salario = 4500  # Atualiza o salário
funcionario.promover('Gerente')  # Atualiza o cargo
funcionario.exibir_informacoes()
