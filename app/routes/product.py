import logging
from flask import Blueprint, request, jsonify, current_app, render_template
import pyodbc
from app.database import get_db_connection

product_bp = Blueprint('product', __name__)

# Настроим базовое логирование для Flask
logging.basicConfig(level=logging.DEBUG)

@product_bp.route('/product-detail', methods=['GET'])
def show_product_detail():
    return render_template('product-detail.html')

@product_bp.route('/product-detail/checkout', methods=['POST'])
def checkout():
    try:
        data = request.get_json()
        cart_items = data.get('cartItems', [])
        email = data.get('email', '')

        if not cart_items:
            return jsonify({"message": "Корзина пуста"}), 400

        # Получаем соединение с базой данных
        conn = get_db_connection()
        cursor = conn.cursor()

        for item in cart_items:
            product_name = item['name']
            sku = item['sku']
            price = item['price']
            quantity = item['quantity']
            total_sum = price * quantity

            # Формируем SQL-запрос для добавления заказа в базу данных
            query = """
            INSERT INTO orders (email, product_name, sku, price, quantity, total_sum)
            VALUES (?, ?, ?, ?, ?, ?)
            """
            # Выполнение запроса
            cursor.execute(query, (email, product_name, sku, price, quantity, total_sum))

        # Фиксируем изменения и закрываем соединение
        conn.commit()
        cursor.close()
        conn.close()

        # Логируем успешную обработку
        logging.info(f"Заказ успешно оформлен для пользователя: {email}")

        return jsonify({"message": "Заказ успешно оформлен!"}), 200
    except Exception as e:
        # Логируем ошибку
        logging.error(f"Ошибка при обработке заказа: {str(e)}")
        return jsonify({"message": "Произошла ошибка при оформлении заказа"}), 500
