from flask import Flask, render_template, request, redirect, flash, url_for
from sqlalchemy import text
from flask_sqlalchemy import SQLAlchemy
from forms import cadastroForm, loginForm
from flask_login import LoginManager, login_user, UserMixin, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from flask_migrate import Migrate


app = Flask(__name__)
app.config['SECRET_KEY'] = 'JHBJDJMBDKJ677898'

# Configurações do MySQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Mylooksql2024@localhost/PetMatch'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializar o banco de dados
db = SQLAlchemy(app)
migrate = Migrate(app, db)  # Configurar Flask-Migrate

# Inicializar o LoginManager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'  # Definir a rota de login

# Função para carregar o usuário baseado no ID
@login_manager.user_loader
def load_user(user_id):
    return Usuario.query.get(int(user_id))

# Modelos de Dados
class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    primeiro_nome = db.Column(db.String(100), nullable=False)
    sobrenome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    senha = db.Column(db.String(200), nullable=False)  # Lembre-se de hashear a senha
    telefone = db.Column(db.String(20), nullable=False)
    rua = db.Column(db.String(150), nullable=False)
    complemento = db.Column(db.String(150), nullable=False)
    cep = db.Column(db.String(9), nullable=False)
    numero = db.Column(db.String(10), nullable=False)
    ddd = db.Column(db.String(2), nullable=False)
    celular = db.Column(db.String(9), nullable=False)
    foto_perfil = db.Column(db.String(300))  # Caminho da foto de perfil, opcional

    def check_password(self, password):
        return check_password_hash(self.senha, password)

    @property
    def is_active(self):
        return True

    @property
    def is_authenticated(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)

class Animal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    especie = db.Column(db.String(50), nullable=False)
    idade = db.Column(db.Integer)
    descricao = db.Column(db.String(300))
    foto = db.Column(db.String(300))  # Caminho da foto


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
                return redirect(url_for('petsList'))
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
            foto_perfil=form.fotoPerfil.data.filename if form.fotoPerfil.data else None
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


@app.route('/recuperar')
def recuperar():
    return render_template('recuperarSenha.html')

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

# Lista de pets com imagem e descrição
pets = [
    {'image': 'pet 1.jpg', 'description': 'Cachorro brincalhão'},
    {'image': 'pet 2.jpg', 'description': 'Gato curioso'},
    # Adicione mais pets conforme necessário...
]

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    print("Tabelas criadas com sucesso!")
    app.run(debug=True)
