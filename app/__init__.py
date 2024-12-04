from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .routes import account, register

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)

    with app.app_context():
        # Регистрация маршрутов
        from .routes import account, register
        app.register_blueprint(account.bp)
        app.register_blueprint(register.bp)

        # Создание таблиц в базе данных (если их нет)
        db.create_all()

    return app
