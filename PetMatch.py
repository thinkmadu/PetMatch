from flask import Flask,render_template

app = Flask(__name__)


@app.route('/login')
def login():
    return render_template('auth/login.html')

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')

#flask --app PetMatch.py run

if __name__ == '__main__':
    app.run(debug=True)