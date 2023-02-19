from flask import Flask, render_template, request, url_for, redirect
from app import *

app = Flask(__name__)

@app.route('/')

def index():
    return render_template('index.html')

@app.route("/acao", methods=['POST'])

def acao():
    
    numero_ticket = request.form.get('Número do ticket')
    ticket = Ticket(numero_ticket)

    if ticket.Existe():
        try:
            ticket.Pesquisar()
        except Exception as e:
            return f"houve um erro: {e}"
    else:
        try:
            ticket.Criar()
        except Exception as e:
            return f"houve um erro: {e}"

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run()