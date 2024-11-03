from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, FileField,IntegerField,TextAreaField,SelectField
from wtforms.validators import DataRequired, Email, EqualTo, Length, Regexp,NumberRange,Optional
from flask_wtf.file import FileAllowed
from config.models import Ong 

class cadastroForm(FlaskForm):
    primeiroNome = StringField('Primeiro Nome', validators=[DataRequired()])
    sobrenome = StringField('Sobrenome', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired()])
    senhaConfirmar = PasswordField('Confirmar Senha', validators=[DataRequired(), EqualTo('senha', message="Senhas diferentes")])
    foto_perfil = FileField('Foto de Perfil', validators=[DataRequired(),FileAllowed(['jpg', 'png', 'jpeg'])])
    rua = StringField('Rua', validators=[DataRequired()])
    complemento = StringField('Complemento', validators=[DataRequired()])
    cep = StringField('CEP', validators=[DataRequired(), Regexp(regex=r'^\d{8}$', message='O CEP deve ter 8 dígitos.'), Length(min=8, max=8)])
    numero = StringField('Número', validators=[DataRequired(), Regexp(regex=r'^\d+$', message='O número deve conter apenas dígitos.')])
    ddd = StringField('DDD', validators=[DataRequired(), Regexp(regex=r'^\d{2}$', message='O DDD deve ter 2 dígitos.'),Length(min=2, max=2)])
    celular = StringField('Celular', validators=[DataRequired(), Regexp(regex=r'^\d{9}$', message='O celular deve ter 9 dígitos.'), Length(min=9, max=9)])
    
    descricao_foto_perfil  = TextAreaField('Descrição da foto de perfil para acessibilidade', validators=[DataRequired(), Length(max=300)])
    
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
    foto_perfil = FileField('Foto de Perfil', validators=[DataRequired(),FileAllowed(['jpg', 'png', 'jpeg'])])
    rua = StringField('Rua')
    complemento = StringField('Complemento')
    cep = StringField('CEP', validators=[ Regexp(regex=r'^\d{8}$', message='O CEP deve ter 8 dígitos.'), Length(min=8, max=8)])
    numero = StringField('Número', validators=[ Regexp(regex=r'^\d+$', message='O número deve conter apenas dígitos.')])
    ddd = StringField('DDD', validators=[Regexp(regex=r'^\d{2}$', message='O DDD deve ter 2 dígitos.'),Length(min=2, max=2)])
    celular = StringField('Celular', validators=[ Regexp(regex=r'^\d{9}$', message='O celular deve ter 9 dígitos.'), Length(min=9, max=9)])
    
    descricao_foto_perfil  = TextAreaField('Descrição da foto de perfil para acessibilidade', validators=[DataRequired(), Length(max=300)])

    
    salvarBotao = SubmitField('Salvar')


class cadastrar_OngForm(FlaskForm):
    nome_Ong = StringField('Nome da ONG', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired()])
    senhaConfirmar = PasswordField('Confirmar Senha', validators=[DataRequired(), EqualTo('senha', message="Senhas diferentes")])
    
    rua = StringField('Rua', validators=[DataRequired()])
    complemento = StringField('Complemento')
    cep = StringField('CEP', validators=[DataRequired(), Regexp(regex=r'^\d{8}$', message='O CEP deve ter 8 dígitos.'), Length(min=8, max=8)])
    cnpj = StringField('CNPJ', validators=[DataRequired(), Regexp(regex=r'^\d{14}$', message='O CNPJ deve ter 14 dígitos.'), Length(min=14, max=14)])
    instagram = StringField('Instagram', validators=[DataRequired()])
    dados_bancarios = StringField('Dados Bancários', validators=[DataRequired()])
    numero = StringField('Número', validators=[DataRequired(), Regexp(regex=r'^\d+$', message='O número deve conter apenas dígitos.')])
    ddd = StringField('DDD', validators=[DataRequired(), Regexp(regex=r'^\d{2}$', message='O DDD deve ter 2 dígitos.'),Length(min=2, max=2)])
    celular = StringField('Celular', validators=[DataRequired(), Regexp(regex=r'^\d{9}$', message='O celular deve ter 9 dígitos.'), Length(min=9, max=9)])
    
    #fotos
    fotoQrCode= FileField('Qr code para doações', validators=[FileAllowed(['jpg', 'png', 'jpeg'])])
    descricao_fotoqrCode = TextAreaField('Descrição do qr code', validators=[DataRequired(), Length(max=300)])
    fotoPerfilLogo = FileField('Foto de Perfil/Logo', validators=[FileAllowed(['jpg', 'png', 'jpeg'])])
    descricao_foto_perfil_Logo = TextAreaField('Descrição da Logo para acessibilidade', validators=[DataRequired(), Length(max=300)])

    cadastrarBotao = SubmitField('Cadastrar ONG')

    def process(self, formdata=None, obj=None, data=None, extra_filters=None):
        # Chama o método `process` padrão do FlaskForm
        super().process(formdata, obj, data, extra_filters)
        
        # Preenche a descrição do QR code automaticamente se `nome_Ong` estiver definido
        if self.nome_Ong.data:
            self.descricao_fotoqrCode.data = f"Essa imagem é o QR code do PIX da ONG {self.nome_Ong.data}"


class AnimalForm(FlaskForm):
    nome = StringField('Nome do Animal', validators=[DataRequired(), Length(min=2, max=100)])

    # Campo especie com opções fixas
    especie = SelectField('Espécie', choices=[('gato', 'Gato'), ('cachorro', 'Cachorro'),('outro','Outro')], validators=[DataRequired()])

    # Campo tamanho com opções fixas
    tamanho = SelectField('Tamanho', choices=[('pequeno', 'Pequeno'), ('medio', 'Médio'), ('grande', 'Grande')],
                          validators=[DataRequired()])

    idade = IntegerField('Idade', validators=[DataRequired(), NumberRange(min=0, max=30, message='Idade inválida')])
    descricao = TextAreaField('Descrição', validators=[DataRequired(), Length(max=300)])
    status = SelectField('Status', choices=[('disponível', 'Disponível'), ('adotado', 'Adotado'),('reservado', 'Reservado')], validators=[DataRequired()])

    foto1 = FileField('Foto 1', validators=[FileAllowed(['jpg', 'png', 'jpeg'], 'Apenas arquivos de imagem são permitidos'), DataRequired()])
    foto2 = FileField('Foto 2', validators=[FileAllowed(['jpg', 'png', 'jpeg'])])
    foto3 = FileField('Foto 3', validators=[FileAllowed(['jpg', 'png', 'jpeg'])])
    foto4 = FileField('Foto 4', validators=[FileAllowed(['jpg', 'png', 'jpeg'])])

    descricao_foto1  = TextAreaField('Descrição da foto', validators=[DataRequired(), Length(max=300)])
    descricao_foto2 = TextAreaField('Descrição da Foto 2', validators=[Optional(), Length(max=300)])
    descricao_foto3 = TextAreaField('Descrição da Foto 3', validators=[Optional(), Length(max=300)])
    descricao_foto4 = TextAreaField('Descrição da Foto 4', validators=[Optional(), Length(max=300)])


    # Campo de nome da ONG preenchido automaticamente e oculto
    ong = StringField('ONG', render_kw={'readonly': True}, validators=[DataRequired()])

    cadastrarBotao = SubmitField('Cadastrar Animal')

    def validate(self, extra_validators=None):
        # Executa validações padrão
        if not super(AnimalForm, self).validate():
            return False

        # Verifica se a descrição está presente para as fotos 2, 3 e 4, caso as fotos tenham sido enviadas
        for i in range(2, 5):
            foto_field = getattr(self, f'foto{i}')
            descricao_field = getattr(self, f'descricao_foto{i}')
            
            # Se a foto foi enviada, a descrição é obrigatória
            if foto_field.data and not descricao_field.data:
                descricao_field.errors.append('Descrição é obrigatória se uma imagem foi enviada.')
                return False

        return True


class editAnimalForm(FlaskForm):
    nome = StringField('Nome do Animal', validators=[DataRequired(), Length(min=2, max=100)])
    especie = StringField('Espécie', validators=[DataRequired(), Length(min=2, max=50)])
    idade = IntegerField('Idade', validators=[DataRequired(), NumberRange(min=0, max=30, message='Idade inválida')])
    descricao = TextAreaField('Descrição', validators=[DataRequired(), Length(max=300)])
    status = SelectField('Status', choices=[('disponível', 'Disponível'), ('adotado', 'Adotado'),('reservado', 'Reservado')], validators=[DataRequired()])
    foto1 = FileField('Foto 1', validators=[FileAllowed(['jpg', 'png', 'jpeg'], 'Apenas arquivos de imagem são permitidos'), DataRequired()])
    foto2 = FileField('Foto 2', validators=[FileAllowed(['jpg', 'png', 'jpeg'])])
    foto3 = FileField('Foto 3', validators=[FileAllowed(['jpg', 'png', 'jpeg'])])
    foto4 = FileField('Foto 4', validators=[FileAllowed(['jpg', 'png', 'jpeg'])])

    descricao_foto1  = TextAreaField('Descrição da foto', validators=[DataRequired(), Length(max=300)])
    descricao_foto2 = TextAreaField('Descrição da Foto 2', validators=[Optional(), Length(max=300)])
    descricao_foto3 = TextAreaField('Descrição da Foto 3', validators=[Optional(), Length(max=300)])
    descricao_foto4 = TextAreaField('Descrição da Foto 4', validators=[Optional(), Length(max=300)])


    # Campo de nome da ONG preenchido automaticamente e oculto
    ong = StringField('ONG', render_kw={'readonly': True}, validators=[DataRequired()])

    cadastrarBotao = SubmitField('Salvar')

    def validate(self):
        # Executa validações padrão
        if not super(AnimalForm, self).validate():
            return False

        # Verifica se a descrição está presente para as fotos 2, 3 e 4, caso as fotos tenham sido enviadas
        for i in range(2, 5):
            foto_field = getattr(self, f'foto{i}')
            descricao_field = getattr(self, f'descricao_foto{i}')
            
            # Se a foto foi enviada, a descrição é obrigatória
            if foto_field.data and not descricao_field.data:
                descricao_field.errors.append('Descrição é obrigatória se uma imagem foi enviada.')
                return False

        return True