from flask import jsonify
from app.services.product_service import get_products_by_category_service, get_all_categories_service

def get_products_by_category_controller(category_id):
    """
    Controlador para obtener productos de una categoría específica.
    """
    try:
        products = get_products_by_category_service(category_id)
        return jsonify({'products': products}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def get_all_categories_controller():
    """
    Controlador para obtener todas las categorías.
    """
    try:
        categories = get_all_categories_service()
        return jsonify({"categories": categories}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
