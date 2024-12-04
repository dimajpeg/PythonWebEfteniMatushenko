from flask import Blueprint, request, jsonify, render_template
from app.database import get_db_connection

auth_bp = Blueprint('auth', __name__, url_prefix='/api/auth')

# Маршрут для отображения страницы входа
@auth_bp.route('/signin', methods=['GET'])
def show_sign_in_form():
    return render_template('sign-in.html')

# Маршрут для обработки входа
@auth_bp.route('/signin', methods=['POST'])
def handle_sign_in():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({"error": "Email and password are required"}), 400

    try:
        if validate_user(email, password):
            return jsonify({"message": "Login successful"}), 200
        else:
            return jsonify({"error": "Invalid email or password"}), 403
    except Exception as e:
        return jsonify({"error": f"Error validating user: {str(e)}"}), 500

# Функция для проверки существования пользователя
def validate_user(email, password):
    conn = get_db_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT password FROM Users WHERE email = ?", (email,))
            stored_password = cursor.fetchone()
            if stored_password and stored_password[0].strip() == password.strip():
                return True
            return False
    except Exception as e:
        raise Exception(f"Error checking user existence: {str(e)}")
    finally:
        conn.close()
