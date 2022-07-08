from controlecartao import db


class Cartao(db.Model):
    def __init__(self, id=int, data=str, doc=int, tipo=str, valor=float):
        self.id = id
        self.data = data
        self.doc = doc
        self.tipo = tipo
        self.valor = valor

    def __repr__(self):
        return '<Name %r>' % self.name
