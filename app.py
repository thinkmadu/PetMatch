from flask import Flask, render_template, request, redirect, flash, url_for
from sqlalchemy import text
from flask_sqlalchemy import SQLAlchemy
from config.forms import cadastroForm, loginForm,ResetPasswordForm,sendLinkForm
from flask_login import LoginManager, login_user, UserMixin, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from flask_mail import Mail, Message
from itsdangerous import URLSafeTimedSerializer
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SECRET_KEY'] = 'JHBJDJMBDKJ677898'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:87Amore;;w34@localhost/PetMatch'
# de madu
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Mylooksql2024@localhost/PetMatch'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


app.config['MAIL_SERVER'] = 'smtp.gmail.com'  # Servidor SMTP do Gmail
app.config['MAIL_PORT'] = 587  # Porta para TLS
app.config['MAIL_USE_TLS'] = True  # Habilita TLS
app.config['MAIL_USE_SSL'] = False  # Não usa SSL
app.config['MAIL_USERNAME'] = 'petmatch.adm@gmail.com'  
#app.config['MAIL_PASSWORD'] = 'eett34;;' 
app.config['MAIL_PASSWORD'] = 'kuya dzya toli ygpz' 
mail = Mail(app)
s = URLSafeTimedSerializer(app.secret_key)


from config.models import Usuario

@login_manager.user_loader
def load_user(user_id):
    return Usuario.query.get(int(user_id))

# Rota de teste para verificar a conexão com o banco de dados
@app.route('/test_db')
def test_db():
    try:
        # Executa uma consulta simples
        result = db.session.execute(text('SELECT 1'))
        return "Conexão com o banco de dados bem-sucedida!"
    except Exception as e:
        return f"Erro ao conectar ao banco de dados: {e}"

# Rotas
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = loginForm()
    if form.validate_on_submit():
        print("Formulário validado!")
        email = form.email.data
        senha = form.senha.data

        user = Usuario.query.filter_by(email=email).first()

        if user:
            print("Usuário encontrado:", user.primeiro_nome)
            print("Senha:", user.senha)
            print("Senha fornecida:", senha)

            if user.check_password(senha):
                login_user(user)
                flash('Login bem-sucedido!', 'success')
                return redirect(url_for('user_layout'))
            else:
                print("Senha incorreta.")
                flash('Senha incorreta. Tente novamente.', 'danger')
        else:
            print("Usuário não encontrado.")
            flash('Usuário não encontrado. Verifique o email.', 'danger')

    return render_template('auth/login.html', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()  # Faz logout do usuário
    flash('Você saiu da sua conta.', 'success')
    return redirect(url_for('login'))

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    form = cadastroForm()
    if form.validate_on_submit():
        print("Formulário validado")
        # Hasheando a senha antes de salvar
        senha_hash = generate_password_hash(form.senha.data)

        # Verificar se uma imagem foi enviada
        if form.fotoPerfil.data:
            # Converta a imagem para binário
            foto_binaria = form.fotoPerfil.data.read()
        else:
            foto_binaria = None  # Caso o usuário não envie uma foto

        # Cria novo usuário
        novo_usuario = Usuario(
            primeiro_nome=form.primeiroNome.data,
            sobrenome=form.sobrenome.data,
            email=form.email.data,
            senha=senha_hash,  # Senha hasheada
            telefone=form.celular.data,
            rua=form.rua.data,
            complemento=form.complemento.data,
            cep=form.cep.data,
            numero=form.numero.data,
            ddd=form.ddd.data,
            celular=form.celular.data,
            foto_perfil=foto_binaria
        )

        user = Usuario.query.filter_by(email=form.email.data).first()
        if user:
            flash('Email já cadastrado. Tente outro.', 'danger')
            return redirect(url_for('login'))

        # Adiciona e confirma o usuário no banco de dados
        db.session.add(novo_usuario)
        db.session.commit()

        flash('Cadastro realizado com sucesso!', 'success')
        return redirect(url_for('login'))
    else:
        print("Formulário inválido:", form.errors)
    return render_template('auth/cadastro.html', form=form)

@app.route('/recuperar', methods=['GET', 'POST'])
def recuperar():
    form = sendLinkForm()
    if form.validate_on_submit():
        email = form.email.data

        # Encontrar o usuário pelo email
        user = Usuario.query.filter_by(email=email).first()
        
        if user:
            # Criar o token
            token = s.dumps(email, salt='email-confirm')
            link = url_for('redefinir', token=token, _external=True)

            # Enviar e-mail
            msg = Message('Redefinição de Senha', sender='your-email@example.com', recipients=[email])
            msg.body = f'Seu link para redefinir a senha é: {link}'
            mail.send(msg)

            flash('Um link para redefinir sua senha foi enviado para seu e-mail.', 'success')
            return redirect(url_for('recuperar'))
        else:
            flash('Usuário não encontrado. Verifique o email.', 'danger')

    return render_template('recuperarSenha.html', form=form)


@app.route('/redefinir', methods=['GET', 'POST'])
def redefinir():
    form = ResetPasswordForm()
    if form.validate_on_submit():
        email = form.email.data
        nova_senha = form.senha.data

        # Encontrar o usuário pelo email
        user = Usuario.query.filter_by(email=email).first()

        if user:
            # Atualizar a senha (lembre-se de hashear antes de salvar)
            user.senha = generate_password_hash(nova_senha)

            # Salvar as mudanças no banco de dados
            db.session.commit()

            flash('Sua senha foi redefinida com sucesso!', 'success')
            return redirect(url_for('login'))  # Redirecionar para a página de login após redefinir a senha
        else:
            flash('Usuário não encontrado. Verifique o email.', 'danger')

    return render_template('redefinirSenha.html', form=form)

@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

@app.route('/petsList')
def petsList():
    page = request.args.get('page', 1, type=int)
    per_page = 20
    start = (page - 1) * per_page
    end = start + per_page
    paginated_pets = pets[start:end]
    total_pages = (len(pets) + per_page - 1) // per_page
    return render_template('petsList.html', pets=paginated_pets, page=page, total_pages=total_pages)

@app.route('/ongsList')
def ongsList():
    page = request.args.get('page', 1, type=int)
    per_page = 20
    start = (page - 1) * per_page
    end = start + per_page
    paginated_pets = pets[start:end]
    total_pages = (len(pets) + per_page - 1) // per_page
    return render_template('ongsList.html', pets=paginated_pets, page=page, total_pages=total_pages)

@app.route('/ongs_pages/ong_1')
def ong_1():
    return render_template('ongs_pages/ong_1.html')

@app.route('/ongs_pages/ong_2')
def ong_2():
    return render_template('ongs_pages/ong_2.html')

@app.route('/user_user_layout')
def user_layout():
    return render_template('user_templates/user_layout.html')