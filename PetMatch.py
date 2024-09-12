from flask import Flask, render_template

app = Flask(__name__)

@app.route('/login')
def login():
    return render_template('auth/login.html')

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/cadastro')
def cadastro():
    return render_template('auth/cadastro.html')

@app.route('/ajude')
def ajude():
    return render_template('Ajude.html')

if __name__ == '__main__':
    app.run(debug=True)
