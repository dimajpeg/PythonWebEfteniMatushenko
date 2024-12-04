from flask import Blueprint, render_template

# Создание Blueprint для главной страницы
main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    """
    Главная страница, рендерит файл index.html.
    """
    return render_template('index.html')

# Регистрация Blueprint в приложении
# Не забудьте зарегистрировать blueprint в файле run.py
