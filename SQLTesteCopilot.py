import sqlite3

class BancoDeDados:
    def __init__(self,nome_banco="biblioteca.db"):
        self.nome_banco = nome_banco
        self.conexao = sqlite3.connect(self.nome_banco)
        self.cursor = self.conexao.cursor()

    def fechar(self):
        if self.conexao:
            self.conexao.close()

class Livro:
    def __init__(self,banco):
        self.banco = banco
        self._criar_tabela()

    def _criar_tabela(self):
        self.banco.cursor.execute('''
            CREATE TABLE IF NOT EXISTS livros(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo TEXT NOT NULL,
                autor TEXT NOT NULL    
            )
        ''')
        self.banco.conexao.commit()

    def adicionar(self,titulo,autor):
        self.banco.conexao.execute('''
            INSERT INTO livros(titulo, autor)
            VALUES (?,?)
        ''', (titulo, autor))
        self.banco.conexao.commit()
        print(f"Registro incluido!")

    def listar_todos(self):
        self.banco.cursor.execute('SELECT * FROM livros')
        livros = self.banco.cursor.fetchall()

        if livros:
            for x in livros:
                print(f"ID:{x[0]}, titulo:{x[1]}, autor:{x[2]}")
        else:
            print("Nenhum livro cadastrado")
        
    def buscar_por_id(self, livro_id):
        #print(f"Tipo de livro_id: {type(livro_id)}")  # Adicione esta linha para depuração
        self.banco.cursor.execute('SELECT * FROM livros WHERE id = ?', (livro_id,))
        x = self.banco.cursor.fetchone()
        if x:
          print(f"ID:{x[0]}, Título:{x[1]}, Autor:{x[2]}")
        else: 
            print(f"Registro {livro_id} inexistente.")


    def atualizar(self,livro_id,titulo,autor):
        self.banco.cursor.execute('''
            UPDATE livros
            SET titulo=?, autor=?
            WHERE id=?
        ''', (titulo,autor,livro_id))
        self.banco.conexao.commit()
        print("Atualizado com sucesso")

    def eliminar(self, livro_id):
        self.banco.cursor.execute('DELETE FROM livros WHERE id = ?',(livro_id,))
        self.banco.conexao.commit()
        print("Eliminado com sucesso.")
        print(f"Tipo de livro_id: {type(livro_id)}")

    def zerar_bd(self):
        self.banco.cursor.execute('DELETE FROM livros')
        self.banco.conexao.commit()
        print('Registros zerados.')

banco = BancoDeDados()
livro = Livro(banco)

#livro.buscar_por_id(int(14))

#livro.atualizar(1,"Mazze Runner","James Dashnner") 

#livro.eliminar(int(7))

#livro.zerar_bd()

#=======================================================================================

#livro.adicionar("Maze Runner","James Dashner")
#livro.adicionar("Bird Box", "Josh Malerman")
#livro.adicionar("A Menina Submersa","Caitlín R. Kiernan")

#=======================================================================================

livro.listar_todos()

