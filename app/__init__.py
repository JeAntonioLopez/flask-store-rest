from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Crear la instancia de SQLAlchemy
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # Configuración de la aplicación
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///store.db'  # O la URI de tu base de datos
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Inicializar la base de datos
    db.init_app(app)

    # Importar y registrar rutas
    from app.routes.admin_routes import admin_bp
    from app.routes.product_routes import product_bp

    app.register_blueprint(admin_bp)
    app.register_blueprint(product_bp)


    return app
