class Produto:
    def __init__(self,nome,categoria,preco):
        self.nome= nome
        self.categoria= categoria
        self.__preco= preco

    @property
    def preco(self):
        return self.__preco
    
    @preco.setter
    def preco(self, aumento):
     if aumento > 0:
        self.__preco += aumento
        print(f'Preco atualizado {self.__preco}')
     else:
        print(f'O aumento tem que ser positivo.')

    def exibir_informacoes(self):
        print(f'Nome: {self.nome}')
        print(f'Cargo: {self.categoria}')
        print(f'Salario: {self.__preco}')

produto1 = Produto('shampoo','cabelo',30.0)
produto1.exibir_informacoes()
produto1.preco = -10.0
produto1.exibir_informacoes()
                   

