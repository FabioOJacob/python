import sqlite3


class Banco():
    def __init__(self):
        self.conexao = sqlite3.connect('banco.db')
        self.createTable()

    def createTable(self):
        c = self.conexao.cursor()  # cursor object

        c.execute("""create table if not exists usuarios 
                    (idusuario integer primary key autoincrement ,
                    nome text,
                    telefone text,
                    email text,
                    usuario text,
                    senha text)""")  # cria a tabela com as descrições que serão salvas os dados
        self.conexao.commit()  #salva as alterações
        c.close()  # termina a conexão
