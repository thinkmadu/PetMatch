from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo, Regexp


class cadastroForm(FlaskForm):
    primeiroNome = StringField('Primero Nome', validators=[DataRequired(),Length(min=2,max=12)])
    sobrenome = StringField('Sobrenome', validators=[DataRequired(),Length(min=2,max=12)])
    email = StringField('Email', validators=[DataRequired(),Email()])
    senha = PasswordField('Senha', validators=[DataRequired()])
    senhaConfirmar = PasswordField('Senha Confirmar', validators=[DataRequired(), EqualTo('senha', message="Senhas diferentes")])
    cadastrarBotao = SubmitField('Cadastrar')
    fotoPerfil = FileField('Foto de Perfil', validators=[FileAllowed(['jpg','png','jpeg'])])
    rua = StringField('Rua', validators=[DataRequired()])
    complemento = StringField('Complemento', validators=[DataRequired()])
    cep = StringField('CEP', validators=[DataRequired(),Regexp(regex='^[0-9]$'),Length(min=8,max=8)])
    numero = StringField('Número', validators=[DataRequired(),Regexp(regex='^[0-9]$')])
    ddd = StringField('DDD', validators=[DataRequired(),Regexp(regex='^[0-9]$'),Length(min=2,max=2)])
    celular = StringField('Celular', validators=[DataRequired(),Regexp(regex='^[0-9]$'),Length(min=9,max=9)])