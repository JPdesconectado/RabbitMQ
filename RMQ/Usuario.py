from Sqlite import Sqlite

class Usuarios(object):

    def __init__(self, idusuario = 0, usuario = "", senha = ""):
        self.info = {}
        self.idusuario = idusuario
        self.usuario = usuario
        self.senha = senha


    def insertUser(self):

        banco = Sqlite()
        try:

            c = banco.conexao.cursor()

            c.execute("insert into usuarios (usuario, senha) values ('" + self.usuario + "', '" + self.senha + "')")
            banco.conexao.commit()
            c.close()

            return "Usuário cadastrado com sucesso!"
        except:
            return "Ocorreu um erro na inserção do usuário"

    def updateUser(self):

        banco = Sqlite()
        try:

            c = banco.conexao.cursor()

            c.execute("update usuarios set usuario = '" + self.usuario + "', senha = '" + self.senha +
            "' where idusuario = " + self.idusuario + " ")

            banco.conexao.commit()
            c.close()

            return "Usuário atualizado com sucesso!"
        except:
            return "Ocorreu um erro na alteração do usuário"

    def deleteUser(self):
        banco =  Sqlite()
        try:

            c = banco.conexao.cursor()

            c.execute("delete from usuarios where idusuario = " + self.idusuario + " ")

            banco.conexao.commit()
            c.close()

            return "Usuário excluído com sucesso!"
        except:
            return "Ocorreu um erro na exclusão do usuário"

    def selectUser(self, idusuario):
        banco =  Sqlite()
        try:

            c = banco.conexao.cursor()

            c.execute("select * from usuarios where idusuario = " + idusuario + "  ")

            for linha in c:
                self.usuario = linha[1]
                self.senha = linha[2]
            c.close()

            return "Busca feita com sucesso!"
        except:
            return "Ocorreu um erro na busca do usuário"


    def selectAllUsers(self):
        banco = Sqlite()
        try:

            c = banco.conexao.cursor()

            users = c.execute("select * from usuarios").fetchall()

            for linha in c:
                self.usuario = linha[1]
                self.senha = linha[2]
            c.close()

            return users
        except:
            return "Usuário não encontrado."
