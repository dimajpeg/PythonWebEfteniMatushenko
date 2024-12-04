import os

class Config:
    SQLALCHEMY_DATABASE_URI = (
        f"mssql+pyodbc://{os.getenv('DB_SERVER', 'localhost,1433')}/"
        f"{os.getenv('DB_NAME', 'FoodShop')}?driver=ODBC+Driver+17+for+SQL+Server"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY', 'supersecretkey')

config = Config()
