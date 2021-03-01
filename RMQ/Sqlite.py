import sqlite3

class Sqlite():

    def __init__(self):
        self.conexao = sqlite3.connect('sqlite.db')
        self.createTable()

    def createTable(self):
        c = self.conexao.cursor()

        c.execute("""create table if not exists usuarios (
                    idusuario integer primary key autoincrement,
                    usuario text,
                    senha text)""")
        self.conexao.commit()
        c.close()