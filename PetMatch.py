from app import app, db, socketio

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    print("Tabelas criadas com sucesso!")
    #app.run(debug=True, port=5001)
    #app.run(debug=True)
    socketio.run(app, debug=True, allow_unsafe_werkzeug=True)