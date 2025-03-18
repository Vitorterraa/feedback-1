from data.conexao import Conexao

class Mensagem:
    @staticmethod
    def recuperar_mensagens():
        conexao = Conexao.criar_conexao()
        cursor = conexao.cursor(dictionary=True)

        cursor.execute("SELECT cod_comentario, nome, comentario, data_hora FROM tb_comentarios ORDER BY data_hora DESC")
        mensagens = cursor.fetchall()

        cursor.close()
        conexao.close()
        return mensagens

    @staticmethod
    def cadastrar_mensagem(nome, comentario):
        conexao = Conexao.criar_conexao()
        cursor = conexao.cursor()

        sql = "INSERT INTO tb_comentarios (nome, comentario, data_hora) VALUES (%s, %s, NOW())"
        valores = (nome, comentario)

        cursor.execute(sql, valores)
        conexao.commit()

        cursor.close()
        conexao.close()

    @staticmethod
    def excluir_mensagem(cod_comentario):
        conexao = Conexao.criar_conexao()
        cursor = conexao.cursor()

        sql = "DELETE FROM tb_comentarios WHERE cod_comentario = %s"
        valores = (cod_comentario,)

        cursor.execute(sql, valores)
        conexao.commit()

        cursor.close()
        conexao.close()
