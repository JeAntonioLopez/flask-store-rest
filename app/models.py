from enum import Enum as PyEnum
from . import db

# Enum para controlar los tipos de usuarios
class UserType(PyEnum):
    ADMIN = "ADMIN"
    VENDOR = "VENDOR"

# Tabla asociativa para la relación muchos a muchos entre productos y categorías
product_category = db.Table(
    "product_category",
    db.metadata,
    db.Column("product_id", db.Integer, db.ForeignKey("product.id"), primary_key=True),
    db.Column("category_id", db.Integer, db.ForeignKey("category.id"), primary_key=True)
)

# Modelo User
class User(db.Model):  # Usamos db.Model aquí
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    type = db.Column(db.Enum(UserType), nullable=False)

# Modelo Category
class Category(db.Model):  # Usamos db.Model aquí
    __tablename__ = "category"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False, unique=True)

    # Relación inversa en Category
    products = db.relationship("Product", secondary=product_category, back_populates="categories")

# Modelo Product
class Product(db.Model):  # Usamos db.Model aquí
    __tablename__ = "product"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.Text)
    stock = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)
    categories = db.relationship("Category", secondary=product_category, back_populates="products")

# Configuración de la base de datos
def setup_database():
    # Crear las tablas usando Flask-SQLAlchemy
    db.create_all()

# Ejemplo para crear registros
if __name__ == "__main__":
    from app import create_app
    app = create_app()

    with app.app_context():  # Necesitamos el contexto de la app para interactuar con la base de datos
        # Crear algunos registros de ejemplo
        admin_user = User(username="admin", password="admin123", type=UserType.ADMIN)
        vendor_user = User(username="vendor", password="vendor123", type=UserType.VENDOR)

        category_food = Category(name="Food")
        category_electronics = Category(name="Electronics")

        product_apple = Product(
            name="Apple", description="A red apple", stock=50, price=0.5, categories=[category_food]
        )
        product_laptop = Product(
            name="Laptop", description="A powerful laptop", stock=10, price=1200.0, categories=[category_electronics]
        )

        # Agregar a la base de datos
        db.session.add_all([admin_user, vendor_user, category_food, category_electronics, product_apple, product_laptop])
        db.session.commit()

        # Verificar
        users = User.query.all()
        for user in users:
            print(f"User: {user.username}, Type: {user.type}")

        products = Product.query.all()
        for product in products:
            print(f"Product: {product.name}, Categories: {[category.name for category in product.categories]}")
