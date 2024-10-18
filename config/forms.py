from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, FileField,IntegerField,TextAreaField,SelectField,QuerySelectField
from wtforms.validators import DataRequired, Email, EqualTo, Length, Regexp,NumberRange
from flask_wtf.file import FileAllowed
from config.models import Ong 

class cadastroForm(FlaskForm):
    primeiroNome = StringField('Primeiro Nome', validators=[DataRequired()])
    sobrenome = StringField('Sobrenome', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired()])
    senhaConfirmar = PasswordField('Confirmar Senha', validators=[DataRequired(), EqualTo('senha', message="Senhas diferentes")])
    fotoPerfil = FileField('Foto de Perfil', validators=[FileAllowed(['jpg', 'png', 'jpeg'])])
    rua = StringField('Rua', validators=[DataRequired()])
    complemento = StringField('Complemento', validators=[DataRequired()])
    cep = StringField('CEP', validators=[DataRequired(), Regexp(regex=r'^\d{8}$', message='O CEP deve ter 8 dígitos.'), Length(min=8, max=8)])
    numero = StringField('Número', validators=[DataRequired(), Regexp(regex=r'^\d+$', message='O número deve conter apenas dígitos.')])
    ddd = StringField('DDD', validators=[DataRequired(), Regexp(regex=r'^\d{2}$', message='O DDD deve ter 2 dígitos.'),Length(min=2, max=2)])
    celular = StringField('Celular', validators=[DataRequired(), Regexp(regex=r'^\d{9}$', message='O celular deve ter 9 dígitos.'), Length(min=9, max=9)])
    cadastrarBotao = SubmitField('Cadastrar')

class loginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired()])
    loginBotao = SubmitField('Login')


class ResetPasswordForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired()])
    senhaConfirmar = PasswordField('Confirmar Senha', validators=[DataRequired(), EqualTo('senha', message="Senhas diferentes")])
    redefinirBotao = SubmitField('Redefinir Senha')

class sendLinkForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    sendBotao = SubmitField('Enviar link de recuperação')

class profileForm(FlaskForm):
    editarBotao = SubmitField('Editar perfil')


class editPerfilForm(FlaskForm):
    primeiroNome = StringField('Primeiro Nome')
    sobrenome = StringField('Sobrenome')
    email = StringField('Email', validators=[ Email()])
    senha = PasswordField('Senha')
    senhaConfirmar = PasswordField('Confirmar Senha', validators=[EqualTo('senha', message="Senhas diferentes")])
    fotoPerfil = FileField('Foto de Perfil', validators=[FileAllowed(['jpg', 'png', 'jpeg'])])
    rua = StringField('Rua')
    complemento = StringField('Complemento')
    cep = StringField('CEP', validators=[ Regexp(regex=r'^\d{8}$', message='O CEP deve ter 8 dígitos.'), Length(min=8, max=8)])
    numero = StringField('Número', validators=[ Regexp(regex=r'^\d+$', message='O número deve conter apenas dígitos.')])
    ddd = StringField('DDD', validators=[Regexp(regex=r'^\d{2}$', message='O DDD deve ter 2 dígitos.'),Length(min=2, max=2)])
    celular = StringField('Celular', validators=[ Regexp(regex=r'^\d{9}$', message='O celular deve ter 9 dígitos.'), Length(min=9, max=9)])
    salvarBotao = SubmitField('Salvar')


class cadastrar_OngForm(FlaskForm):
    nome_Ong = StringField('Nome da ONG', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired()])
    senhaConfirmar = PasswordField('Confirmar Senha', validators=[DataRequired(), EqualTo('senha', message="Senhas diferentes")])
    fotoQrCode= FileField('Qr code para doações', validators=[FileAllowed(['jpg', 'png', 'jpeg'])])
    fotoPerfilLogo = FileField('Foto de Perfil/Logo', validators=[FileAllowed(['jpg', 'png', 'jpeg'])])
    rua = StringField('Rua', validators=[DataRequired()])
    complemento = StringField('Complemento')
    cep = StringField('CEP', validators=[DataRequired(), Regexp(regex=r'^\d{8}$', message='O CEP deve ter 8 dígitos.'), Length(min=8, max=8)])
    cnpj = StringField('CNPJ', validators=[DataRequired(), Regexp(regex=r'^\d{14}$', message='O CNPJ deve ter 14 dígitos.'), Length(min=14, max=14)])
    instagram = StringField('Instagram', validators=[DataRequired()])
    dados_bancarios = StringField('Dados Bancários', validators=[DataRequired()])
    numero = StringField('Número', validators=[DataRequired(), Regexp(regex=r'^\d+$', message='O número deve conter apenas dígitos.')])
    ddd = StringField('DDD', validators=[DataRequired(), Regexp(regex=r'^\d{2}$', message='O DDD deve ter 2 dígitos.'),Length(min=2, max=2)])
    celular = StringField('Celular', validators=[DataRequired(), Regexp(regex=r'^\d{9}$', message='O celular deve ter 9 dígitos.'), Length(min=9, max=9)])
    cadastrarBotao = SubmitField('Cadastrar ONG')


class AnimalForm(FlaskForm):
    nome = StringField('Nome do Animal', validators=[DataRequired(), Length(min=2, max=100)])
    especie = StringField('Espécie', validators=[DataRequired(), Length(min=2, max=50)])
    idade = IntegerField('Idade', validators=[DataRequired(), NumberRange(min=0, max=30, message='Idade inválida')])
    descricao = TextAreaField('Descrição', validators=[DataRequired(), Length(max=300)])
    status = SelectField('Status', choices=[('disponível', 'Disponível'), ('adotado', 'Adotado')], validators=[DataRequired()])
    foto1 = FileField('Foto 1', validators=[FileAllowed(['jpg', 'png', 'jpeg'], 'Apenas arquivos de imagem são permitidos'), DataRequired()])
    foto2 = FileField('Foto 2', validators=[FileAllowed(['jpg', 'png', 'jpeg'])])
    foto3 = FileField('Foto 3', validators=[FileAllowed(['jpg', 'png', 'jpeg'])])
    foto4 = FileField('Foto 4', validators=[FileAllowed(['jpg', 'png', 'jpeg'])])

    # Campo para escolher a ONG a qual o animal pertence
    ong = QuerySelectField('ONG', query_factory=lambda: Ong.query.all(), get_label='nome_Ong', allow_blank=False, validators=[DataRequired()])

    cadastrarBotao = SubmitField('Cadastrar Animal')