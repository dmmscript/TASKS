class Livro:
    def __init__(self, titulo, autor, num_paginas):
        self.titulo = titulo
        self.autor = autor
        self.__num_paginas = num_paginas

    @property
    def num_paginas(self):
        return self.__num_paginas

    @num_paginas.setter
    def num_paginas(self, novo_num_paginas):
        if novo_num_paginas > 0:
            self.__num_paginas = novo_num_paginas
            print(f'Número de páginas atualizado para {novo_num_paginas}.')
        else:
            print('O número de páginas deve ser um valor positivo.')

    def exibir_informacoes(self):
        print(f'Título: {self.titulo}')
        print(f'Autor: {self.autor}')
        print(f'Número de Páginas: {self.__num_paginas}')

# Exemplo de uso da classe Livro
livro = Livro('1984', 'George Orwell', 328)
livro.exibir_informacoes()
livro.num_paginas = 350 # Atualiza o número de páginas
livro.exibir_informacoes()