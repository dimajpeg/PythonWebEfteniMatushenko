import pyodbc
import os


def get_db_connection():
    # Настройки подключения из переменных окружения
    server = os.getenv('DB_SERVER', 'localhost,1433')  # Сервер и порт
    database = os.getenv('DB_NAME', 'FoodShop')  # Имя базы данных

    # Подключение с использованием Windows аутентификации
    conn = pyodbc.connect(f'DRIVER={{ODBC Driver 17 for SQL Server}};'
                          f'SERVER={server};'
                          f'DATABASE={database};'
                          'Trusted_Connection=yes')  # Использование Windows аутентификации
    return conn
