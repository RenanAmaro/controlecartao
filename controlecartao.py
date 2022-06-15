
from flask import Flask, render_template, redirect, request

app = Flask(__name__)

lista = []


class Cartao():
    def __init__(self, cod=int, data=str, doc=int, tipo=str, valor=float):
        self.cod = cod
        self.data = data
        self.doc = doc
        self.tipo = tipo
        self.valor = valor


cartao = Cartao(1, '14/06/2022', 1023040, 'Credito', 115.0)
lista.append(cartao)


@app.route('/')
def index():
    return render_template('index.html', titulo='Controle Cartão', jogos=lista)


@app.route('/criar', methods=['POST', ])
def criar():
    cod = request.form['cod']
    data = request.form['data']
    doc = request.form['doc']
    tipo = request.form['tipo']
    valor = request.form['valor']
    cartao = Cartao(cod, data, doc, tipo, valor)
    lista.append(cartao)
    return redirect('/')


app.run(debug=True)
