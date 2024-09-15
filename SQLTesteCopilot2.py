import sqlite3

class BancoDeDados:
    def __init__(self,nome_banco="cinema.db"):
        self.nome_banco = nome_banco
        self.conexao = sqlite3.connect(self.nome_banco)
        self.cursor = self.conexao.cursor()

    def fechar(self):
       if self.conexao:
            self.conexao.close()

class Filme:
    def __init__(self,banco):
       self.banco = banco
       self._criar_tabela()

    def _criar_tabela(self):
        self.banco.cursor.execute('''
            CREATE TABLE IF NOT EXISTS filmes(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo TEXT NOT NULL,
                diretor TEXT NOT NULL,
                ano TEXT NOT NULL)
        ''')
        self.banco.cursor.commit()

    
