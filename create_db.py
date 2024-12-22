from app import create_app, db
from app.models import User, Product, Category, UserType 


app = create_app()


with app.app_context():
    db.create_all()


    if not User.query.first():  
        admin_user = User(username="admin", password="admin123", type=UserType.ADMIN)
        vendor_user = User(username="vendor", password="vendor123", type=UserType.VENDOR)
        db.session.add_all([admin_user, vendor_user])
    
    if not Category.query.first():
        category_food = Category(name="Food")
        category_electronics = Category(name="Electronics")
        db.session.add_all([category_food, category_electronics])
    
    if not Product.query.first():
        category_food = Category.query.filter_by(name="Food").first()
        category_electronics = Category.query.filter_by(name="Electronics").first()
        
        product_apple = Product(name="Apple", description="A red apple", stock=50, price=0.5, categories=[category_food])
        product_laptop = Product(name="Laptop", description="A powerful laptop", stock=10, price=1200.0, categories=[category_electronics])
        db.session.add_all([product_apple, product_laptop])

    db.session.commit()
    print("Database created and populated successfully")
