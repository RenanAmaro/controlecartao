
from flask import Flask, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_pyfile('config.py')


db = SQLAlchemy(app)


class Cartao(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    data = db.Column(db.Date, nullable=False)
    doc = db.Column(db.String(10), nullable=False)
    tipo = db.Column(db.String(100), nullable=False)
    valor = db.Column(db.Float(10), nullable=False)

    def __repr__(self):
        return '<Name %r>' % self.name


@app.route('/')
def index():
    lancamentos = Cartao.query.order_by(Cartao.id)
    print()
    print(lancamentos)
    print()
    
    return render_template('index.html', titulo='Controle Cartão', lancamentos=lancamentos, taxa=1.45)


@app.route('/criar', methods=['POST', ])
def criar():
    id = request.form['id']
    data = request.form['data']
    doc = request.form['doc']
    tipo = request.form['tipo']
    valor = request.form['valor']

    novo_lancamento = Cartao(data=data, doc=doc, tipo=tipo, valor=valor)
    db.session.add(novo_lancamento)
    db.session.commit()

    return redirect('/')


app.run(debug=True)


if __name__ == '__main__':
    app.run(debug=True)
