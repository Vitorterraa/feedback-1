from flask import Flask

app = Flask(__name__)

# Aqui vão as minhas Rotas.

@app.route("/")
def pagina_principal():
    return "MEGA PAGINA PRINCIPAK"

app.run(debug = True)