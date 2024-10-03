from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, FileField
from wtforms.validators import DataRequired, Email, EqualTo, Length, Regexp
from flask_wtf.file import FileAllowed

class cadastroForm(FlaskForm):
    primeiroNome = StringField('Primeiro Nome', validators=[DataRequired()])
    sobrenome = StringField('Sobrenome', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired()])
    senhaConfirmar = PasswordField('Confirmar Senha', validators=[DataRequired(), EqualTo('senha', message="Senhas diferentes")])
    fotoPerfil = FileField('Foto de Perfil', validators=[FileAllowed(['jpg', 'png', 'jpeg'])])
    rua = StringField('Rua', validators=[DataRequired()])
    complemento = StringField('Complemento', validators=[DataRequired()])
    cep = StringField('CEP', validators=[DataRequired(), Regexp(regex=r'^\d{5}-\d{3}$', message='O CEP deve ter 8 dígitos.'), Length(min=9, max=9)])
    numero = StringField('Número', validators=[DataRequired(), Regexp(regex=r'^\d+$', message='O número deve conter apenas dígitos.')])
    ddd = StringField('DDD', validators=[DataRequired(), Regexp(regex=r'^\d{2}$', message='O DDD deve ter 2 dígitos.'),Length(min=2, max=2)])
    celular = StringField('Celular', validators=[DataRequired(), Regexp(regex=r'^\d{9}$', message='O celular deve ter 9 dígitos.'), Length(min=9, max=9)])
    cadastrarBotao = SubmitField('Cadastrar')

class loginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired()])
    loginBotao = SubmitField('Login') 