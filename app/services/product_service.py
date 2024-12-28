from app.models import Category
from app import db

from app.models import Product, Category, product_category
from app import db


def get_products_by_category_service(category_id):
    """
    Get every product of a given category.
    """
    try:
        category = Category.query.get(category_id)

        if not category:
            raise Exception(f"Category {category_id} not found")

        products = db.session.query(Product).join(product_category).filter(
            product_category.c.category_id == category_id).all()

        product_list = [{"id": p.id, "name": p.name,
                         "description": p.description, "price": p.price} for p in products]

        return product_list
    except Exception as e:
        raise Exception(f"Error fetching products: {str(e)}")


def get_all_categories_service():
    """
    Get all categories.
    """
    try:
        categories = Category.query.all()
        return [{"id": category.id, "name": category.name} for category in categories]
    except Exception as e:
        raise Exception(f"Error getting categories: {str(e)}")


def sell_product_service(product_id, quantity):
    """
    Handles selling a product by updating its stock.
    """
    try:
        product = Product.query.get(product_id)
        if not product:
            raise Exception(f"Product with ID {product_id} not found")
        
        if product.stock < quantity:
            raise Exception(f"Not enough stock for product {product.name}. Available: {product.stock}")
        
        # Update stock
        product.stock -= quantity
        db.session.commit()
        
        return {"message": f"Sold {quantity} of {product.name}. Remaining stock: {product.stock}"}
    except Exception as e:
        raise Exception(f"Error selling product: {str(e)}")


def update_stock_service(product_id, new_stock):
    """
    Updates the stock of a product.
    """
    try:
        product = Product.query.get(product_id)
        if not product:
            raise Exception(f"Product with ID {product_id} not found")
        
        product.stock = new_stock
        db.session.commit()
        
        return {"message": f"Stock updated to {new_stock} for product {product.name}"}
    except Exception as e:
        raise Exception(f"Error updating stock: {str(e)}")

def update_price_service(product_id, new_price):
    """
    Updates the price of a product.
    """
    try:
        product = Product.query.get(product_id)
        if not product:
            raise Exception(f"Product with ID {product_id} not found")
        
        product.price = new_price
        db.session.commit()
        
        return {"message": f"Price updated to {new_price} for product {product.name}"}
    except Exception as e:
        raise Exception(f"Error updating price: {str(e)}")
