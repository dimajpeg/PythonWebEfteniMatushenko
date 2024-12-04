from app.routes.register import register_bp

def register_blueprints(app):
    app.register_blueprint(register_bp)



