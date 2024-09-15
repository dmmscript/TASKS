class Funcionario:

    def __init__(self,nome,cargo,salario):
        self.nome= nome
        self.cargo= cargo
        self.__salario= salario

    @property
    def salario(self):
     return self.__salario

    @salario.setter
    def salario(self, aumento):
        if aumento > 0.0:
            self.__salario += aumento
            print(f'Salário atualizado {self.__salario}')
        else:
            print('O aumento deve ser positivo')

    def exibir_informacoes(self):
        print(f'Nome: {self.nome}')
        print(f'Cargo: {self.cargo}')
        print(f'Salario: {self.__salario}')

func1 = Funcionario('Dani','estudante',3000.0)
func1.exibir_informacoes()
func1.salario = 500.0
func1.exibir_informacoes

    

    