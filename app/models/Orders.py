from app.database import get_db_connection

db = get_db_connection()

class Order(db.Model):
    __tablename__ = 'orders'

    Idividual_Order_id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # Поле индивидуального ID
    order_id = db.Column(db.String(100), nullable=False)  # Общий ID для заказа
    email = db.Column(db.String(50), nullable=False)  # Email пользователя
    product_id = db.Column(db.Integer, nullable=False)  # ID товара
    total_sum = db.Column(db.Integer, nullable=False)  # Общая сумма заказа

