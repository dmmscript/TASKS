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


class Biblioteca:
    def __init__(self):  #INSTANCIANDO
        self.__livros = [] #LISTA

    def adicionar_livro(self, livro):
        if isinstance(livro, Livro):
            self.__livros.append(livro)
            print(f'Livro "{livro.titulo}" adicionado à biblioteca.')
        else:
            print('O objeto adicionado não é um Livro.')

    def remover_livro(self, titulo):
        for livro in self.__livros:
            if livro.titulo == titulo:
                self.__livros.remove(livro)
                print(f'Livro "{titulo}" removido da biblioteca.')
                return
        print(f'Livro "{titulo}" não encontrado.')

    def listar_livros(self):
        if not self.__livros:
            print('Nenhum livro na biblioteca.')
        for livro in self.__livros:
            livro.exibir_informacoes()
            print('---')

# Exemplo de uso da classe Biblioteca
biblioteca = Biblioteca()
livro1 = Livro('1984', 'George Orwell', 328)
livro2 = Livro('Brave New World', 'Aldous Huxley', 288)

biblioteca.adicionar_livro(livro1)
biblioteca.adicionar_livro(livro2)
biblioteca.listar_livros()
biblioteca.remover_livro('1984')
biblioteca.listar_livros()
