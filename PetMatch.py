from app import app, db

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
    #app.run(debug=True, port=5001)
    app.run(debug=True)