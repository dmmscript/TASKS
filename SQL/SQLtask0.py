import sys
import os

# Adiciona o caminho da pasta 'DATABASE' ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'DATABASE')))

from DBtask0 import BancoDeDados

class Pessoa:
    def __init__(self,banco):
        self.banco = banco # inicializa a classe com uma conexao
        self._criar_tabela() # chama o metodo _criar_tabela()

    def _criar_tabela(self):
        self.banco.cursor.execute('''
            CREATE TABLE IF NOT EXISTS pessoas(
                id INTEGER PRIMARY KEY AUTOINCREMENT, 
                nome TEXT NOT NULL,
                fone TEXT NOT NULL
            )
        ''')
        self.banco.conexao.commit()
        '''
self.banco.cursor.execute: Este comando recebe uma clausula SQL.
As clausulas que usaremos começam com Create, Select, Insert, Uptade e Delete
Create - cria uma tabela
Select - seleciona registros
Insert - inclui registros
Uptade - atualiza/altera registros
Delete - elimina registros
Com exceção da clausula Select, todas as demais tem que terminar com o comando abaixo.
self.banco.conexao.commit()
Este comando confirma as manipulações pretendidas anteriormente
'''
    def adicionar(self,nome,fone):
        self.banco.conexao.execute('''
            INSERT INTO pessoas(nome,fone)
            VALUES (?,?)
        ''', (nome,fone))
        self.banco.conexao.commit()
        print("Registro incluido.")

    def listar_todos(self):
        self.banco.cursor.execute('SELECT * FROM pessoas')
        pessoas = self.banco.cursor.fetchall() #buscar-todos
        if pessoas:
            for x in pessoas:
                print(f"ID:{x[0]}, Nome:{x[1]}, Fone:{x[2]}")
        else:
            print("Nenhuma pessoa cadastrada.")

    def buscar_por_id(self,pessoa_id):
         print(f"Tipo de pessoa_id: {type(pessoa_id)}")  # Adicione esta linha para depuração
         self.banco.cursor.execute('SELECT * FROM pessoas WHERE id = ?',(pessoa_id,))
         x = self.banco.cursor.fetchone() #buscar-um
         if x:
             print(f"ID:{x[0]}, Nome:{x[1]}, Fone:{x[2]}")
         else:
            print(f"Registro {pessoa_id} não existente.")
    
    def atualizar(self,pessoa_id,nome,fone):
        self.banco.cursor.execute('''
            UPDATE pessoas
            SET nome=?, fone=?
            WHERE id=?
        ''',(nome,fone,pessoa_id))
        self.banco.conexao.commit()
        print("Atualizado com sucesso.")

    def remover(self,pessoa_id):
        self.banco.cursor.execute('DELETE FROM pessoas WHERE id = ?',(pessoa_id,))
        self.banco.conexao.commit()
        print("Eliminado com sucesso.")

    def remover_todos(self):
        self.banco.cursor.execute('DELETE FROM pessoas')
        self.banco.conexao.commit()
        print("Todos os registros foram eliminados com sucesso")

banco = BancoDeDados()
pessoa = Pessoa(banco)

#pessoa.adicionar("Danielly","16988064132")
#pessoa.adicionar("João","16997889356")

#pessoa.atualizar(1,"Danielly","01988064132")

#pessoa.adicionar("Dani","876867")
#pessoa.adicionar("Joao","727927")
#pessoa.adicionar("Lais","4747878")

pessoa.listar_todos()