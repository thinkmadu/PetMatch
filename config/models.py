from datetime import datetime
import random

from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, UserMixin, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import event

from PetMatch import db


#criação dos admins - executado só uma vez
""" INSERT	INTO admin(id,nome,email,senha)
 VALUES (44,"Dua Lipa","admin1@gmail.com","77"),(74,"Olivia Rodrigo","admin2@gmail.com","88"),
(48,"Beyonce","admin3@gmail.com","77"),(24,"Sia","admin4@gmail.com","88");
"""

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
    foto_perfil =db.Column(db.String(300), nullable=False)
    #descrição das fotos para acessibilidade
    descricao_foto_perfil = db.Column(db.String(300), nullable=False)


    # relacionamento com Adocao
    adocoes = db.relationship('Adocao', back_populates='usuario', lazy=True)


    def check_password(self, password):
        return check_password_hash(self.senha, password)


class Mensagem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String(500), nullable=False)  # Texto da mensagem
    sender_name = db.Column(db.String(100), nullable=False)  # Nome do remetente
    room_id = db.Column(db.Integer, db.ForeignKey('animal.id'), nullable=False)  # Referência ao animal
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)  # Hora de envio

    # relacionamento com animal
    animal = db.relationship('Animal', backref=db.backref('mensagens', lazy=True))

    def __repr__(self):
        return f"<Mensagem {self.sender_name}: {self.message}>"


class InteresseAnimal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)
    animal_id = db.Column(db.Integer, db.ForeignKey('animal.id'), nullable=False)
    numero_unico = db.Column(db.String(10), unique=True, nullable=False)  # Número único
    data_interesse = db.Column(db.DateTime, default=datetime.utcnow)

    # Relacionamentos
    usuario = db.relationship('Usuario', backref=db.backref('interesses', lazy=True))
    animal = db.relationship('Animal', backref=db.backref('interesses', lazy=True))

class Animal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    especie = db.Column(db.String(50), nullable=False)
    tamanho = db.Column(db.String(20), nullable=False)
    idade = db.Column(db.Integer, nullable=False)
    descricao = db.Column(db.String(300), nullable=False)

    status = db.Column(db.String(50), nullable=False)

    #fotos
    foto1  = db.Column(db.String(200), nullable=False)
    foto2 = db.Column(db.String(200))
    foto3 = db.Column(db.String(200))
    foto4 = db.Column(db.String(200))

    #descrição das fotos para acessibilidade
    descricao_foto1 = db.Column(db.String(300), nullable=False)
    descricao_foto2 = db.Column(db.String(300), nullable=True)
    descricao_foto3 = db.Column(db.String(300), nullable=True)
    descricao_foto4 = db.Column(db.String(300), nullable=True)


    # foreign key para referenciar a ONG
    ong_id = db.Column(db.Integer, db.ForeignKey('ong.id'), nullable=False)

    #  relacionamento com  Ong
    ong = db.relationship('Ong', backref='animais')

    # relacionamento com Adocao (para acessar o adotante)
    adocao = db.relationship('Adocao', back_populates='animal', uselist=False, lazy=True)

    @property
    def adotante(self):
        adotacao = Adocao.query.filter_by(animal_id=self.id).first()
        if adotacao:
            return adotacao.usuario  # Retorna o usuário (adotante) associado
        return None


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
    dados_bancarios = db.Column(db.String(100), nullable=False)

    #fotos
    foto_perfil_Logo = db.Column(db.String(200), nullable=True)
    foto_qrCode =db.Column(db.String(200), nullable=True)

    #descrição das fotos para acessibilidade
    descricao_foto_perfil_Logo = db.Column(db.String(300), nullable=False)
    descricao_foto_qrCode = db.Column(db.String(300), nullable=False)

    def check_password(self, password):
        return check_password_hash(self.senha, password)


class Adocao(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)
    animal_id = db.Column(db.Integer, db.ForeignKey('animal.id'), nullable=False)
    data_adocao = db.Column(db.DateTime, default=datetime.utcnow)

    # relacionamento com Usuario
    usuario = db.relationship('Usuario', back_populates='adocoes')

    # relacionamento com Animal
    animal = db.relationship('Animal', back_populates='adocao')
