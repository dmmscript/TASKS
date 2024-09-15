import os
import sqlite3
    
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, 'DBtask0.db')

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
    def __init__(self,nome_banco=DB_PATH):
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