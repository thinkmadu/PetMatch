
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, UserMixin, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import event

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

# admins que criei
#(44,"Dua Lipa","admin1@gmail.com","77"),
#(74,"Olivia Rodrigo","admin2@gmail.com","88")

# INSERT	INTO admin(id,nome,email,senha)
# VALUES (44,"Dua Lipa","admin1@gmail.com","77"),(74,"Olivia Rodrigo","admin2@gmail.com","88");
# (48,"Beyonce","admin3@gmail.com","77"),(24,"Sia","admin4@gmail.com","88");

class Admin(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    senha = db.Column(db.String(200), nullable=False)

    def check_password(self, password):
        return check_password_hash(self.senha, password)


class Ong(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    nome_Ong = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    senha = db.Column(db.String(200), nullable=False)
    telefone = db.Column(db.String(20), nullable=False)
    rua = db.Column(db.String(150), nullable=False)
    complemento = db.Column(db.String(150), nullable=False)
    cep = db.Column(db.String(9), nullable=False)
    instagram = db.Column(db.String(50), nullable=False)
    cnpj = db.Column(db.String(14), nullable=False)
    numero = db.Column(db.String(10), nullable=False)
    ddd = db.Column(db.String(2), nullable=False)
    celular = db.Column(db.String(9), nullable=False)
    foto_perfil_Logo = db.Column(db.LargeBinary, nullable=False)
    foto_qrCode = db.Column(db.LargeBinary, nullable=False)
    dados_bancarios = db.Column(db.String(100), nullable=False)

    def check_password(self, password):
        return check_password_hash(self.senha, password)
