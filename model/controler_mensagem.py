import datetime
from data.conexao import Conexao

class Mensagem:
    def cadastrar_mensagem(usuario, mensagem):
    
        data_hora = datetime.datetime.today()

        conexao = Conexao.criar_conexao()
    
        cursor = conexao.cursor()

        sql = "INSERT INTO tb_comentarios(nome,data_hora, comentario) VALUES(%s,%s,%s)"

        valores = (usuario, data_hora, mensagem)

        cursor.execute(sql, valores)

        conexao.commit()

        cursor.close()

        conexao.close()
        
    def recuperar_mensagens():
        
        conexao = Conexao.criar_conexao()
        
        cursor = conexao.cursor(dictionary= True)
        
        sql = """SELECT nome as usuario, comentario as mensagem, data_hora FROM tb_comentarios"""
        
        cursor.execute(sql)
        
        resultado = cursor.fetchall()
        
        cursor.close()
        
        conexao.close()
        
        return resultado
    

        