from flask import Blueprint, render_template

# Создание Blueprint для страниц
boys_and_marvel_bp = Blueprint('boys_and_marvel', __name__)

# Список всех маршрутов с соответствующими HTML-шаблонами
routes = [
    ('/boys-but.html', 'boys-but.html'),
    ('/boys-houm.html', 'boys-houm.html'),
    ('/boys-sol.html', 'boys-sol.html'),
    ('/boys-star.html', 'boys-star.html'),
    ('/dc-batman.html', 'dc-batman.html'),
    ('/future-dc-batmult.html', 'future-dc-batmult.html'),
    ('/classic-dc-batsoski.html', 'classic-dc-batsoski.html'),
    ('/dc-joker.html', 'dc-joker.html'),
    ('/dc-hq.html', 'dc-hq.html'),
    ('/boys_and_marvel/marvel-ant-man.html', 'marvel-ant-man.html'),
    ('/marvel-spider-man.html', 'marvel-spider-man.html'),
    ('/marvel-women-spidy.html', 'marvel-women-spidy.html'),
    ('/marvel-kwon.html', 'marvel-kwon.html'),
    ('/marvel-wolverine.html', 'marvel-wolverine.html'),
    ('/wars-luk.html', 'wars-luk.html'),
    ('/wars-bf.html', 'wars-bf.html'),
    ('/wars-dart.html', 'wars-dart.html'),
    ('/wars-an.html', 'wars-an.html'),
    ('/wars-chui.html', 'wars-chui.html')
]

# Добавляем маршруты с уникальными endpoint
for route, template in routes:
    endpoint_name = template.replace('.', '_')  # Заменяем точки на подчеркивания
    boys_and_marvel_bp.add_url_rule(
        route,
        endpoint=endpoint_name,  # Уникальный endpoint без точки
        view_func=lambda tpl=template: render_template(tpl)
    )
