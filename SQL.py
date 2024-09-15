import sqlite3
'''
Roteiro 11.09.2024
===========
Parte I
Criar um bando de dados (BD) de nome: Agenda
Criar uma tabela de nome: pessoa
Criar três atributos (campos): id, nome, telefone
===========
Parte II
Criar uma classe para criar/conectar/fechar o BD
===========
Parte III
Criar uma classe com metodos que irão executar o CRUD
(C)reate - Criar registros
(R)ead - Ler registros (listar)
(U)pdate - Atualizar registros
(D)elete - Eliminar registros
=========================================================
SQL - Manipulação de um Banco de Dados
*Ainda não aprendemos, vamos aprender
=========================================================
db = data base = bd = banco de dados
Banco de Dados = agenda.db
'''
class BancoDeDados:
    def __init__(self,nome_banco="agenda.db"):
        self.nome_banco = nome_banco
        self.conexao = sqlite3.connect(self.nome_banco)
        self.cursor = self.conexao.cursor()

    def fechar(self):
        if self.conexao:
            self.conexao.close()

'''
sqlite3.connect(self.nome_banco): Cria/abre um BD.
self.conexao: O objeto que representa/conecta o BD.
self.conexao.cursor(): É um ponteiro/cursor que aponta para um registro.
self.cursor: O objeto que representa o cursor/ponteiro.
self.conexao.close(): Encerra a conexão 
'''
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