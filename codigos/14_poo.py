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


class Departamento:
    def __init__(self):
        self.__funcionarios = []

    def adicionar_funcionario(self, funcionario):
        if isinstance(funcionario, Funcionario):
            self.__funcionarios.append(funcionario)
            print(f'Funcionário "{funcionario.nome}" adicionado ao departamento.')
        else:
            print('O objeto adicionado não é um Funcionário.')

    def remover_funcionario(self, nome):
        for funcionario in self.__funcionarios:
            if funcionario.nome == nome:
                self.__funcionarios.remove(funcionario)
                print(f'Funcionário "{nome}" removido do departamento.')
                return
        print(f'Funcionário "{nome}" não encontrado.')

    def listar_funcionarios(self):
        if not self.__funcionarios:
            print('Nenhum funcionário no departamento.')
        for funcionario in self.__funcionarios:
            funcionario.exibir_informacoes()
            print('---')

# Exemplo de uso da classe Departamento
departamento = Departamento()
funcionario1 = Funcionario('João Bosco', 'Desenvolvedor Backend', 10000.0)
funcionario2 = Funcionario('Ana Maria', 'Desenvolvedor Frontend', 7000.0)

departamento.adicionar_funcionario(funcionario1)
departamento.adicionar_funcionario(funcionario2)
departamento.listar_funcionarios()
departamento.remover_funcionario('Ana Maria')
departamento.listar_funcionarios()
