import sys
import os

# Adiciona o caminho da pasta 'DATABASE' ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'DATABASE')))

from DBtask2 import BancoDeDados

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
        self.banco.conexao.commit()

    def adicionar(self,titulo,diretor,ano):
        self.banco.cursor.execute('''
            INSERT INTO filmes(titulo,diretor,ano)
            VALUES (?,?,?)
        ''', (titulo,diretor,ano))
        self.banco.conexao.commit()
        print("Registro incluido.")

    def visualizar(self):
        self.banco.cursor.execute('SELECT * FROM filmes')
        filmes = self.banco.cursor.fetchall()
        if filmes:
            for x in filmes:
                print(f"ID:{x[0]}, titulo:{x[1]}, diretor:{x[2]}, ano:{x[3]}")
        else:
            print("Nenhum filme cadastrado.")

    def buscar_por_id(self,filme_id):
        self.banco.cursor.execute('SELECT * FROM filmes WHERE id = ?',(filme_id,))
        filme_id = self.banco.cursor.fetchone()
        if filme_id:
            print(f"ID:{x[0]}, titulo:{x[1]}, diretor:{x[2]}, ano:{c[3]}")
        else:
            print(f"{filme_id} - Registro inexistente.")

    def atualizar(self,filme_id,titulo,diretor,ano):
          self.banco.cursor.execute('''
            UPTADE filmes
            SET titulo=?, diretor=?, ano=?
            WHERE id=?
          ''', (titulo,diretor,ano,filme_id))
          self.banco.conexao.commit()
          print("Atualizado com sucesso.")  

    def remover(self,filme_id):
        self.banco.cursor.execute('DELETE FROM filmes WHERE id=?',(filme_id,))
        self.banco.conexao.commit()
        print("Removido com sucesso.")

    def reset(self):
        self.banco.cursor.execute("DELETE FROM sqlite_sequence WHERE name = 'filmes'")
        self.banco.conexao.commit()
        print("Resetado com sucesso.")



banco = BancoDeDados()
filme = Filme(banco)

#filme.adicionar("O poderoso chefão","Francis Ford Coppola","1972")

#filme.buscar_por_id(int(1))

#filme.visualizar()

#filme.remover(int(1))

#filme.visualizar()

#filme.reset()