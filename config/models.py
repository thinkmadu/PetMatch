
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, UserMixin, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash

from PetMatch import db

class Usuario(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    primeiro_nome = db.Column(db.String(100), nullable=False)
    sobrenome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    senha = db.Column(db.String(200), nullable=False)
    telefone = db.Column(db.String(20), nullable=False)
    rua = db.Column(db.String(150), nullable=False)
    complemento = db.Column(db.String(150), nullable=False)
    cep = db.Column(db.String(9), nullable=False)
    numero = db.Column(db.String(10), nullable=False)
    ddd = db.Column(db.String(2), nullable=False)
    celular = db.Column(db.String(9), nullable=False)
    foto_perfil = db.Column(db.LargeBinary)

    def check_password(self, password):
        return check_password_hash(self.senha, password)

class Animal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    especie = db.Column(db.String(50), nullable=False)
    idade = db.Column(db.Integer)
    descricao = db.Column(db.String(300))
    foto = db.Column(db.LargeBinary)
