from flask import Flask, render_template,  request, redirect, flash, url_for
from flask_sqlalchemy import SQLAlchemy
from forms import cadastroForm,loginForm
app = Flask(__name__)
app.config['SECRET_KEY'] = 'JHBJDJMBDKJ677898'

#sql lite

db_name = 'PetMatch.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+db_name
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# Inicializar o banco de dados
db = SQLAlchemy(app)

@app.route('/login')
def login():
    form = loginForm()
    return render_template('auth/login.html', form=loginForm())

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    form = cadastroForm()
    if form.validate_on_submit():
        # Aqui você processa os dados do formulário e salva no banco de dados
        novo_usuario = Usuario(
            primeiro_nome=form.primeiroNome.data,
            sobrenome=form.sobrenome.data,
            email=form.email.data,
            senha=form.senha.data,  # Lembre-se de hashear a senha
            telefone=form.celular.data
        )
        db.session.add(novo_usuario)
        db.session.commit()
        flash('Cadastro realizado com sucesso!', 'success')
        return redirect('auth/login.html')  # Redireciona para a página de login após cadastro
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


class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    primeiro_nome = db.Column(db.String(100), nullable=False)
    sobrenome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    senha = db.Column(db.String(200), nullable=False)
    telefone = db.Column(db.String(20), nullable=False)

class Animal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    especie = db.Column(db.String(50), nullable=False)
    idade = db.Column(db.Integer)
    descricao = db.Column(db.String(300))
    foto = db.Column(db.String(300))  # Caminho da foto

# Lista de pets com imagem e descrição
pets = [
    {'image': 'pet1.jpg', 'description': 'Cachorro brincalhão'},
    {'image': 'pet2.jpg', 'description': 'Gato curioso'},
    # Adicione mais pets conforme necessário...
]

if __name__ == '__main__':
    app.run(debug=True)