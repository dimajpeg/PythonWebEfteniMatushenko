from flask import Flask
from config import config
from app.database import get_db_connection
from app.routes.register import register_bp  # Импорт маршрута для регистрации
from app.routes.auth import auth_bp  # Импорт маршрута для аутентификации
from app.routes.main import main_bp  # Импорт нового маршрута
from app.routes.product import product_bp
from app.routes.products import products_bp  # Импортируем маршрут для продуктов
from app.routes.boys_and_marvel import boys_and_marvel_bp
from app.routes.account import account_bp


def create_app():
    """
    Фабрика приложения Flask для инициализации приложения.
    """
    app = Flask(__name__)
    app.config.from_object(config)

    # Проверка подключения к базе данных при запуске приложения
    check_db_connection()

    # Регистрация маршрутов
    app.register_blueprint(register_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(main_bp)
    app.register_blueprint(product_bp)
    app.register_blueprint(products_bp)
    app.register_blueprint(boys_and_marvel_bp)
    app.register_blueprint(account_bp)
    return app

def check_db_connection():
    """
    Функция для проверки подключения к базе данных.
    """
    try:
        conn = get_db_connection()
        conn.close()
        print("Подключение к базе данных успешно установлено.")
    except Exception as e:
        print(f"Ошибка подключения к базе данных: {e}")
        raise

if __name__ == "__main__":
    app = create_app()

    try:
        app.run(debug=True)
    except Exception as e:
        print(f"Ошибка при запуске приложения: {e}")
