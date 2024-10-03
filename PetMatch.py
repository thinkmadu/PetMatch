from flask import Flask, render_template, request, redirect, flash, url_for
from sqlalchemy import text 
from flask_sqlalchemy import SQLAlchemy
from forms import cadastroForm, loginForm
from flask_login import LoginManager, login_user, UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)
app.config['SECRET_KEY'] = 'JHBJDJMBDKJ677898'



# Configurações do MySQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:87Amore;;w34@localhost/PetMatch'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


# Inicializar o banco de dados
db = SQLAlchemy(app)

# Modelos de Dados
class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    primeiro_nome = db.Column(db.String(100), nullable=False)
    sobrenome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    senha = db.Column(db.String(200), nullable=False)  # Lembre-se de hashear a senha
    telefone = db.Column(db.String(20), nullable=False)

    def check_password(self, password):
        return check_password_hash(self.senha, password)

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
        email = form.email.data
        senha = form.senha.data  # Use 'senha' ao invés de 'password'
        
        # Tente encontrar o usuário no banco de dados
        user = Usuario.query.filter_by(email=email).first()
        
        if user and user.check_password(senha):  # Verifique se você tem um método check_password no modelo Usuario
            login_user(user)  # Faz login do usuário
            print("Usuário logado com sucesso!")
            flash('Login bem-sucedido!', 'success')  # Mensagem de sucesso
            return redirect(url_for('home'))  # Redireciona para a página inicial ou outra página
        else:
            print("Email ou senha incorretos.")
            flash('Email ou senha incorretos. Tente novamente.', 'danger')  # Mensagem de erro

    return render_template('auth/login.html', form=form)

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    form = cadastroForm()
    if form.validate_on_submit():
        print("Formulário validado")
        # Cria novo usuário
        novo_usuario = Usuario(
            primeiro_nome=form.primeiroNome.data,
            sobrenome=form.sobrenome.data,
            email=form.email.data,
            senha=form.senha.data,  # Lembre-se de hashear a senha
            telefone=form.celular.data
        )
        user = novo_usuario.query.filter_by(email=form.email.data).first()
        if user:
            flash('Email já cadastrado. Tente outro.', 'danger')
            return redirect(url_for('login'))
        # Adiciona e confirma o usuário no banco de dados
        db.session.add(novo_usuario)
        db.session.commit()

        flash('Cadastro realizado com sucesso!', 'success')
        return redirect(url_for('login'))  # Redireciona para a página de login após cadastro
    else:
        print("Formulário inválido:", form.errors)
    return render_template('auth/cadastro.html', form=form)

@app.route('/recuperar')
def recuperar():
    return render_template('recuperarSenha.html')

@app.route('/ajude')
def ajude():
    return render_template('Ajude.html')

@app.route('/petsList')
def petsList():
    page = request.args.get('page', 1, type=int)
    per_page = 20
    start = (page - 1) * per_page
    end = start + per_page
    paginated_pets = pets[start:end]
    total_pages = (len(pets) + per_page - 1) // per_page
    return render_template('petsList.html', pets=paginated_pets, page=page, total_pages=total_pages)

# Lista de pets com imagem e descrição
pets = [
    {'image': 'pet1.jpg', 'description': 'Cachorro brincalhão'},
    {'image': 'pet2.jpg', 'description': 'Gato curioso'},
    # Adicione mais pets conforme necessário...
]

if __name__ == '__main__':
    with app.app_context():
     db.create_all()
     print("Tabelas criadas com sucesso!")
    app.run(debug=True)
