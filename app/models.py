from enum import Enum as PyEnum
from . import db

class UserType(PyEnum):
    ADMIN = "ADMIN"
    VENDOR = "VENDOR"

product_category = db.Table(
    "product_category",
    db.metadata,
    db.Column("product_id", db.Integer, db.ForeignKey("product.id"), primary_key=True),
    db.Column("category_id", db.Integer, db.ForeignKey("category.id"), primary_key=True)
)

class User(db.Model): 
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    type = db.Column(db.Enum(UserType), nullable=False)

class Category(db.Model): 
    __tablename__ = "category"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False, unique=True)

    products = db.relationship("Product", secondary=product_category, back_populates="categories")

class Product(db.Model):  
    __tablename__ = "product"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.Text)
    stock = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)
    categories = db.relationship("Category", secondary=product_category, back_populates="products")

def setup_database():
    db.create_all()

if __name__ == "__main__":
    from app import create_app
    app = create_app()

    with app.app_context():  
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

        db.session.add_all([admin_user, vendor_user, category_food, category_electronics, product_apple, product_laptop])
        db.session.commit()

        users = User.query.all()
        for user in users:
            print(f"User: {user.username}, Type: {user.type}")

        products = Product.query.all()
        for product in products:
            print(f"Product: {product.name}, Categories: {[category.name for category in product.categories]}")
