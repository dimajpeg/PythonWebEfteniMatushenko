from flask import Blueprint, request, jsonify, render_template
from app.database import get_db_connection

# Создание Blueprint для регистрации
register_bp = Blueprint('register', __name__, url_prefix='/api/users')


# === Регистрация ===

@register_bp.route('/sign-up.html', methods=['GET'])
def show_signup_page():
    """
    Отображение страницы регистрации.
    """
    return render_template('sign-up.html')


@register_bp.route('/signup', methods=['POST'])
def handle_register():
    """
    Обработка регистрации нового пользователя.
    """
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    confirm_password = data.get('confirm_password')

    if not email or not password or not confirm_password:
        return jsonify({"error": "Email, password, and confirm_password are required"}), 400

    if password != confirm_password:
        return jsonify({"error": "Passwords do not match"}), 400

    if user_exists(email):
        return jsonify({"error": "Email is already registered"}), 400

    try:
        create_user(email, password)
        return jsonify({"message": "User registered successfully"}), 201
    except Exception as e:
        return jsonify({"error": "An error occurred during registration"}), 500


# === Вспомогательные функции ===

def user_exists(email):
    """
    Проверка существования пользователя по email.
    """
    try:
        conn = get_db_connection()
        with conn.cursor() as cursor:
            cursor.execute("SELECT COUNT(*) FROM Users WHERE email = ?", (email,))
            return cursor.fetchone()[0] > 0
    except Exception as e:
        print(f"Error checking user existence: {e}")
        return False
    finally:
        conn.close()


def create_user(email, password):
    """
    Создание нового пользователя в базе данных.
    """
    try:
        conn = get_db_connection()
        with conn.cursor() as cursor:
            cursor.execute("INSERT INTO Users (email, password) VALUES (?, ?)", (email, password))
            conn.commit()
    except Exception as e:
        print(f"Error creating user: {e}")
        raise
    finally:
        conn.close()
