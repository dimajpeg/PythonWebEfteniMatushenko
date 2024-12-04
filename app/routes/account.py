from flask import Blueprint, request, jsonify, render_template
from app.database import get_db_connection

account_bp = Blueprint('account', __name__)


@account_bp.route('/account', methods=['GET'])
def show_account():
    email = request.args.get('email')
    print(f"[DEBUG] Email для аккаунта: {email}")

    if not email:
        return render_template('error.html', message="Email is required")

    return render_template('my-account.html', email=email)
# Маршрут для отображения страницы аккаунта
@account_bp.route('/my-account', methods=['POST'])
def get_account_data():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    print(f"[DEBUG] Полученный email: {email}")
    print(f"[DEBUG] Полученный пароль: {password}")

    if not email or not password:
        return jsonify({'error': 'Email and password are required'}), 400

    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        # Проверка пользователя
        cursor.execute("SELECT password FROM Users WHERE email = ?", (email,))
        user_data = cursor.fetchone()

        if not user_data:
            print("[DEBUG] Пользователь не найден")
            return jsonify({'error': 'User not found'}), 404

        stored_password = user_data[0]
        if stored_password.strip() != password.strip():
            print("[DEBUG] Неверный пароль")
            return jsonify({'error': 'Invalid password'}), 403

        # Запрос для получения заказов (с использованием id)
        cursor.execute("""
            SELECT id, total_sum, product_name, quantity
            FROM orders
            WHERE email = ?
        """, (email,))
        orders = cursor.fetchall()

        # Преобразование данных заказов в список
        orders_list = [
            {
                'orderId': order[0],  # Используем id из таблицы
                'totalCost': order[1],
                'products': order[2],
                'quantity': order[3],
            }
            for order in orders
        ]

        print(f"[DEBUG] Заказы: {orders_list}")

        return jsonify({
            'email': email,
            'password': password,
            'orders': orders_list
        }), 200

    except Exception as e:
        print(f"[ERROR] Ошибка сервера: {e}")
        return jsonify({'error': f"Error fetching account data: {str(e)}"}), 500
