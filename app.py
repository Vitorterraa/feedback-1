from flask import Flask, render_template, request, redirect
import datetime
import mysql.connector
from data.conexao import Conexao
from model.controler_mensagem import Mensagem

app = Flask(__name__)

# Aqui vão as minhas Rotas.

@app.route("/")
def pagina_principal():
    return render_template("index.html")

@app.route("/post/cadastrar_mensagem", methods = ["POST"])
def post_mensagem():
    usuario = request.form.get("usuario")
    mensagem = request.form.get("comentario")
    
    
    
    Mensagem.cadastrar_mensagem(usuario, mensagem)
    
    return redirect("/")
    

app.run(debug = True)