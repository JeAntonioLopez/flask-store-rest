from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///store.db' 
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    from app.routes.admin_routes import admin_bp
    from app.routes.product_routes import product_bp
    from app.routes.auth_routes import auth_bp
    
    app.register_blueprint(admin_bp)
    app.register_blueprint(product_bp)
    app.register_blueprint(auth_bp)


    return app
