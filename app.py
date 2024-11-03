from flask import Flask, render_template, request, redirect, flash, url_for,current_app
from sqlalchemy import text
from werkzeug.utils import secure_filename
import os
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, UserMixin, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from flask_mail import Mail, Message
from itsdangerous import URLSafeTimedSerializer
from flask_migrate import Migrate
import base64


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads' 
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


from config.models import Usuario, Admin, Ong, Animal
from config.forms import cadastroForm, loginForm,ResetPasswordForm,sendLinkForm,profileForm,editPerfilForm,cadastrar_OngForm,AnimalForm,editAnimalForm


@login_manager.user_loader
def load_user(user_id):
    # Tenta carregar como Admin
    user = Admin.query.get(int(user_id))
    if user:
        return user

    # Tenta carregar como Ong
    user = Ong.query.get(int(user_id))
    if user:
        return user

    # Tenta carregar como Usuario
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

        print("Email:", email)
        print("Senha:", senha)

        user = Usuario.query.filter_by(email=email).first()

        if user:
            print("Usuário encontrado:", user.primeiro_nome)
            print("Senha:", user.senha)
            print("Senha fornecida:", senha)

            if user.check_password(senha):
                login_user(user)
                flash('Login bem-sucedido!', 'success')
                return redirect(url_for('profile'))
            else:
                print("Senha incorreta.")
                flash('Senha incorreta. Tente novamente.', 'danger')

        # Verifica na tabela Admin
        admin = Admin.query.filter_by(email=email).first()
        if admin and admin.check_password(senha):
            login_user(admin)
            flash('Login bem-sucedido! Bem-vindo Admin.', 'success')
            return redirect(url_for('admin_dashboard'))  # Redireciona para o dashboard do admin

        # Verifica na tabela Ong
        ong = Ong.query.filter_by(email=email).first()
        if ong and ong.check_password(senha):
            login_user(ong)
            flash('Login bem-sucedido! Bem-vindo Ong.', 'success')
            return redirect(url_for('ong_dashboard'))  # Redireciona para a página da ONG

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

       # Inicializa a variável para o caminho da foto do perfil
        foto_perfil_path = None

        # Verifica se uma imagem foi enviada
        if form.foto_perfil.data:
            # Salva a imagem na pasta de uploads
            filename = secure_filename(form.foto_perfil.data.filename)
            foto_perfil_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            form.foto_perfil.data.save(foto_perfil_path)

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
            foto_perfil=foto_perfil_path,  # Caminho da imagem
            descricao_foto_perfil=form.descricao_foto_perfil.data
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

@app.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    form = profileForm()
    if isinstance(current_user, Usuario):
        if form.validate_on_submit():
            return redirect(url_for('edit_profile'))
        return render_template('user_pages/profile.html', form=form)


@app.route('/profile/edit', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = editPerfilForm()
    if isinstance(current_user, Usuario):

# Verifique se o usuário tem uma foto de perfil
        foto_perfil_atual = None
        if current_user.foto_perfil:
            # Obtenha o caminho da foto de perfil atual
            foto_perfil_atual = current_user.foto_perfil

        # Preencher o formulário com os dados atuais do usuário logado
        if request.method == 'GET':
            form.primeiroNome.data = current_user.primeiro_nome
            form.sobrenome.data = current_user.sobrenome
            form.email.data = current_user.email
            form.rua.data = current_user.rua
            form.complemento.data = current_user.complemento
            form.cep.data = current_user.cep
            form.numero.data = current_user.numero
            form.descricao_foto_perfil.data = current_user.descricao_foto_perfil
            form.ddd.data = current_user.ddd
            form.celular.data = current_user.celular
        
        # Quando o formulário for submetido
        if form.validate_on_submit():
            current_user.primeiro_nome = form.primeiroNome.data
            current_user.sobrenome = form.sobrenome.data
            current_user.email = form.email.data
            current_user.rua = form.rua.data
            current_user.complemento = form.complemento.data
            current_user.cep = form.cep.data
            current_user.descricao_foto_perfil = form.descricao_foto_perfil.data
            current_user.numero = form.numero.data
            current_user.ddd = form.ddd.data
            current_user.celular = form.celular.data

            # Se uma nova foto de perfil for enviada
            if form.foto_perfil.data:

                if current_user.foto_perfil and os.path.exists(current_user.foto_perfil):
                    os.remove(current_user.foto_perfil)
                filename = secure_filename(form.foto_perfil.data.filename)
                foto_perfil_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                form.foto_perfil.data.save(foto_perfil_path)
                current_user.foto_perfil = foto_perfil_path  # Armazena o caminho no banco de dados

            # Se uma nova senha for fornecida
            if form.senha.data:
                current_user.senha = generate_password_hash(form.senha.data)

            # Salvar as alterações no banco de dados
            db.session.commit()

            flash('Perfil atualizado com sucesso!', 'success')
            return redirect(url_for('profile'))

    return render_template('user_pages/edit.html', form=form, foto_perfil_atual=foto_perfil_atual)

# @app.route('/petsList')
# def petsList():
#     animais = Animal.query.all()
#     page = request.args.get('page', 1, type=int)
#     per_page = 20
#     start = (page - 1) * per_page
#     end = start + per_page
#     paginated_pets = pets[start:end]
#     total_pages = (len(pets) + per_page - 1) // per_page
#     return render_template('petsList.html', pets=paginated_pets, page=page, total_pages=total_pages)


@app.route('/petsList')
def petsList():
    page = request.args.get('page', 1, type=int)
    per_page = 20
    animais = Animal.query.paginate(page=page, per_page=per_page, error_out=False)
    total_pages = animais.pages

    return render_template('petsList.html', animal=animais.items, page=page, total_pages=total_pages)


# @app.route('/ongsList')
# def ongsList():
#     page = request.args.get('page', 1, type=int)
#     per_page = 20
#     start = (page - 1) * per_page
#     end = start + per_page
#     paginated_pets = pets[start:end]
#     total_pages = (len(pets) + per_page - 1) // per_page
#     return render_template('ongsList.html')
@app.route('/ongsList')
def ongsList():
    page = request.args.get('page', 1, type=int)  # Obter o número da página da requisição
    per_page = 5
    ongs = Ong.query.paginate(page=page, per_page=per_page, error_out=False)  # Consultar ONGs no banco de dados
    total_pages = ongs.pages  # Obter o total de páginas

    return render_template('ongsList.html', ongs=ongs.items, page=page, total_pages=total_pages)


@app.route('/ongs_pages/ong_1')
def ong_1():
    return render_template('ongs_pages/ong_1.html')

@app.route('/ongs_pages/ong_2')
def ong_2():
    return render_template('ongs_pages/ong_2.html')

@app.route('/user_user_layout')
def user_layout():
    return render_template('user_templates/user_layout.html')



# ROTAS DO ADMIN

@app.route('/admin_dashboard')
@login_required
def admin_dashboard():
    # Verifica se o usuário logado é um administrador
    print(isinstance(current_user, Admin))
    
    if isinstance(current_user, Admin):
        # Aqui você pode adicionar dados que deseja exibir no dashboard
        usuarios = Usuario.query.all()
        ongs = Ong.query.all()
        animais = Animal.query.all()
        return render_template('admin_pages/admin_dashboard.html', usuarios=usuarios, ongs=ongs,animais=animais)
    else:
        print("Acesso negado. Somente administradores podem acessar esta página.")
        flash('Acesso negado. Somente administradores podem acessar esta página.', 'danger')
        return redirect(url_for('home'))

@app.route('/admin_dashboard/ongs_register', methods=['GET', 'POST'])
@login_required
def ongs_register():
    # Verifica se o usuário logado é um administrador
    if isinstance(current_user, Admin):
        form = cadastrar_OngForm()

         # Processa o formulário antes de validar
        form.process(formdata=request.form)

        if form.validate_on_submit():
            print("Formulário validado")
            
            
            # Hasheando a senha antes de salvar
            senha_hash = generate_password_hash(form.senha.data)
            
            # Caminhos das imagens a serem salvas
            foto_qr_code_path = None
            foto_perfil_path = None

            # Verifica e salva a imagem do QR code
            if form.fotoQrCode.data:
                filename_qr = secure_filename(form.fotoQrCode.data.filename)
                foto_qr_code_path = os.path.join(app.config['UPLOAD_FOLDER'], filename_qr)
                form.fotoQrCode.data.save(foto_qr_code_path)

            # Verifica e salva a imagem do perfil/logo
            if form.fotoPerfilLogo.data:
                filename_logo = secure_filename(form.fotoPerfilLogo.data.filename)
                foto_perfil_path = os.path.join(app.config['UPLOAD_FOLDER'], filename_logo)
                form.fotoPerfilLogo.data.save(foto_perfil_path)

            # Cria nova ONG
            nova_ong = Ong(
                nome_Ong=form.nome_Ong.data,
                email=form.email.data,
                senha=senha_hash,  # Senha hasheada
                telefone=form.celular.data,
                rua=form.rua.data,
                complemento=form.complemento.data,
                cep=form.cep.data,
                numero=form.numero.data,
                ddd=form.ddd.data,
                celular=form.celular.data,
                foto_perfil_Logo=foto_perfil_path,
                foto_qrCode=foto_qr_code_path,
                cnpj=form.cnpj.data,
                instagram=form.instagram.data,
                dados_bancarios=form.dados_bancarios.data,
                descricao_foto_perfil_Logo=form.descricao_foto_perfil_Logo.data,
                descricao_foto_qrCode=form.descricao_fotoqrCode.data
            )


            # Verifica se a ONG já existe pelo email
            ong_existente = Ong.query.filter_by(email=form.email.data).first()
            if ong_existente:
                flash('Email já cadastrado. Tente outro.', 'danger')
                return redirect(url_for('ongs_register'))

            # Adiciona e confirma a ONG no banco de dados
            db.session.add(nova_ong)
            db.session.commit()

            flash('Cadastro de ONG realizado com sucesso!', 'success')
            return redirect(url_for('admin_dashboard'))

        else:
            print("Formulário inválido:", form.errors)

        return render_template('admin_pages/ongs_register.html', form=form)

    else:
        flash('Acesso negado. Apenas administradores podem acessar esta página.', 'danger')
        return redirect(url_for('home'))


# ROTAS DA ONG

@app.route('/ong_dashboard')
@login_required
def ong_dashboard():

    # Verifica se o usuário logado é um administrador
    print(isinstance(current_user, Ong))
    
    if isinstance(current_user, Ong):
        # Aqui você pode adicionar dados que deseja exibir no dashboard

        animais = Animal.query.filter_by(ong_id=current_user.id).all()
        return render_template('ongs_pages/ong_dashboard.html',animais=animais)
    else:
        print("Acesso negado. Somente Ongs podem acessar esta página.")
        flash('Acesso negado. Somente Ongs podem acessar esta página.', 'danger')
        return redirect(url_for('home'))
    

@app.route('/ong_dashboard/pets_register', methods=['GET', 'POST'])
@login_required
def pets_register():
    # Verifica se o usuário logado é uma ONG
    if isinstance(current_user, Ong):
        form = AnimalForm()

        # Preenche o campo ong com o nome da ONG associada
        form.ong.data = current_user.nome_Ong

        if form.validate_on_submit():
            # Diretório de upload
            upload_folder = current_app.config['UPLOAD_FOLDER']
            os.makedirs(upload_folder, exist_ok=True)

            # Salva as imagens e armazena o caminho no banco de dados
            foto_paths = []
            for i in range(1, 5):
                foto = getattr(form, f'foto{i}').data
                if foto:
                    filename = secure_filename(foto.filename)
                    foto_path = os.path.join(upload_folder, filename)
                    foto.save(foto_path)
                    foto_paths.append(foto_path)  # Adiciona o caminho para o banco
                else:
                    foto_paths.append(None)  # Se não houver imagem, adiciona None

            # Criando novo animal
            novo_animal = Animal(
                nome=form.nome.data,
                especie=form.especie.data,
                tamanho = form.tamanho.data,
                idade=form.idade.data,
                descricao=form.descricao.data,
                status=form.status.data,
                foto1=foto_paths[0],
                foto2=foto_paths[1],
                foto3=foto_paths[2],
                foto4=foto_paths[3],
                descricao_foto1=form.descricao_foto1.data,
                descricao_foto2=form.descricao_foto2.data,
                descricao_foto3=form.descricao_foto3.data,
                descricao_foto4=form.descricao_foto4.data,
                ong_id=current_user.id
            )


            # Adiciona e salva o novo animal no banco de dados
            db.session.add(novo_animal)
            db.session.commit()

            flash('Animal cadastrado com sucesso!', 'success')
            return redirect(url_for('ong_dashboard'))
        else:
            print("Formulário inválido:", form.errors)

        return render_template('ongs_pages/pets_register.html', form=form)
    
    else:
        flash('Acesso negado. Apenas ONGs podem acessar esta página.', 'danger')
        return redirect(url_for('home'))


@app.route('/ong_dashboard/pets_delete/<int:id>', methods=['POST'])
@login_required
def delete_animal(id):
    if isinstance(current_user, Ong):
        animal = Animal.query.get_or_404(id)  # Busca o animal pelo ID

         # Exclui as imagens associadas ao animal
        for foto_path in [animal.foto1, animal.foto2, animal.foto3, animal.foto4]:
            if foto_path and os.path.exists(foto_path):  # Verifica se o caminho existe
                os.remove(foto_path)  # Exclui a imagem

        db.session.delete(animal)  # Exclui o animal do banco de dados
        db.session.commit()  # Confirma a exclusão
        flash('Animal excluído com sucesso!', 'success')
        return redirect(url_for('ong_dashboard'))
    else:
        flash('Acesso negado. Apenas ONGs podem acessar esta página.', 'danger')
        return redirect(url_for('home'))
    
@app.route('/ong_dashboard/pets_edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_animal(id):
    if isinstance(current_user, Ong):
        animal = Animal.query.get_or_404(id)  # Busca o animal pelo ID
        form = editAnimalForm()

        # Preenche o campo ong com o nome da ONG associada
        form.ong.data = current_user.nome_Ong

        # Preenche o formulário com os dados atuais do animal
        if request.method == 'GET':
            form.nome.data = animal.nome
            form.especie.data = animal.especie
            form.tamanho.data = animal.tamanho
            form.idade.data = animal.idade
            form.descricao.data = animal.descricao
            form.status.data = animal.status

        # Processa o formulário ao submeter
        if form.validate_on_submit():
            # Atualiza os campos do animal
            animal.nome = form.nome.data
            animal.especie = form.especie.data
            animal.tamanho = form.tamanho.data
            animal.idade = form.idade.data
            animal.descricao = form.descricao.data
            animal.status = form.status.data

            # Atualiza as fotos se novas forem enviadas
            for i, foto_field in enumerate([form.foto1, form.foto2, form.foto3, form.foto4], start=1):
                if foto_field.data:
                    # Deleta a imagem antiga
                    foto_atual = getattr(animal, f'foto{i}')
                    if foto_atual and os.path.exists(foto_atual):
                        os.remove(foto_atual)

                    # Salva a nova imagem
                    filename = secure_filename(foto_field.data.filename)
                    path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                    foto_field.data.save(path)
                    setattr(animal, f'foto{i}', path)

            # Salvar as alterações no banco de dados
            db.session.commit()

            flash('Animal atualizado com sucesso!', 'success')
            return redirect(url_for('ong_dashboard'))  # Redireciona para o dashboard da ONG

        return render_template('ongs_pages/pets_edit.html', form=form, animal=animal)
    else:
        flash('Acesso negado. Apenas ONGs podem acessar esta página.', 'danger')
        return redirect(url_for('home'))