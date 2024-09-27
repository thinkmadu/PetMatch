from PetMatch import db, app

# Garante que o contexto da aplicação está ativo
with app.app_context():
    # Cria todas as tabelas no banco de dados

    db.create_all()
