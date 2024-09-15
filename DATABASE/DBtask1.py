import os
import sqlite3
    
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, 'DBtask1.db')

class BancoDeDados:
    def __init__(self,nome_banco=DB_PATH):
        self.nome_banco = nome_banco
        self.conexao = sqlite3.connect(self.nome_banco)
        self.cursor = self.conexao.cursor()

    def fechar(self):
        if self.conexao:
            self.conexao.close()
