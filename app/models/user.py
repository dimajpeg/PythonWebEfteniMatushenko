from app.database import get_db_connection


class User(get_db_connection.Model):
    __tablename__ = 'users'
    user_id = get_db_connection.Column(get_db_connection.Integer, primary_key=True, autoincrement=True)
    email = get_db_connection.Column(get_db_connection.String(50), nullable=False, unique=True)
    password = get_db_connection.Column(get_db_connection.String(100), nullable=False)
