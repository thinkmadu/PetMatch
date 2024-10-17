from werkzeug.security import generate_password_hash
from app import db ,app
from config.models import Admin

# Atualize as senhas dos administradores
with app.app_context():
    admins = Admin.query.all()
    for admin in admins:
        admin.senha = generate_password_hash(admin.senha)
        db.session.add(admin)
    db.session.commit()