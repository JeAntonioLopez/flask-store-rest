from app.models import Category
from app import db

from app.models import Product, Category, product_category
from app import db

def get_products_by_category_service(category_id):
    """
    Obtiene todos los productos de una categoría específica.
    """
    try:
        # Obtener la categoría por su ID
        category = Category.query.get(category_id)
        
        if not category:
            raise Exception(f"Categoría con ID {category_id} no encontrada")
        
        # Obtener los productos que pertenecen a esta categoría utilizando la tabla intermedia
        products = db.session.query(Product).join(product_category).filter(product_category.c.category_id == category_id).all()
        
        # Formatear la lista de productos
        product_list = [{"id": p.id, "name": p.name, "description": p.description, "price": p.price} for p in products]
        
        return product_list
    except Exception as e:
        raise Exception(f"Error al obtener los productos: {str(e)}")



def get_all_categories_service():
    """
    Obtiene todas las categorías disponibles.
    """
    try:
        # Obtener todas las categorías
        categories = Category.query.all()
        
        # Retornar una lista con los nombres y IDs de las categorías
        return [{"id": category.id, "name": category.name} for category in categories]
    except Exception as e:
        raise Exception(f"Error al obtener las categorías: {str(e)}")
