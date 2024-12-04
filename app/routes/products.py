from flask import Blueprint, request, jsonify, render_template
from app.database import get_db_connection

# Blueprint для обработки продуктов
products_bp = Blueprint('products', __name__, url_prefix='/products')

# Маршрут для отображения страницы продуктов
@products_bp.route('/products.html', methods=['GET'])
def show_products():
    return render_template('products.html')

# Маршрут для поиска продукта
@products_bp.route('/products.html', methods=['POST'])
def search_product():
    data = request.get_json()
    query = data.get('query', '').strip()

    if not query:
        return jsonify({'error': 'Search term is required'}), 400

    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        # Запрос к базе данных
        cursor.execute("""
            SELECT product_link
            FROM products
            WHERE product_name LIKE ?
        """, (f"%{query}%",))
        result = cursor.fetchone()

        cursor.close()
        conn.close()

        if result:
            # Возвращаем ссылку из базы данных без изменений
            product_link = result[0].strip()
            return jsonify({'link': product_link})
        else:
            return jsonify({'error': 'No matching products found.'}), 404

    except Exception as e:
        print(f"[ERROR] Ошибка при поиске продукта: {e}")
        return jsonify({'error': 'An error occurred while searching for the product.'}), 500


