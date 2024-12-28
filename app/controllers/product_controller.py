from flask import jsonify, request
from app.services.product_service import get_products_by_category_service, get_all_categories_service, sell_product_service, update_price_service, update_stock_service
from app.middlewares.middlewares import can_sell, is_admin

@can_sell
def get_products_by_category_controller(category_id):
    """
    Controller to get products of a given category.
    """
    try:
        products = get_products_by_category_service(category_id)
        return jsonify({'products': products}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@can_sell
def get_all_categories_controller():
    """
    Controller to get all categories.
    """
    try:
        categories = get_all_categories_service()
        return jsonify({"categories": categories}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@can_sell
def sell_product_controller(product_id):
    """
    Controller to handle selling a product.
    """
    try:
        data = request.get_json()
        quantity = data.get("quantity", 0)

        if quantity <= 0:
            return jsonify({"error": "Invalid quantity"}), 400

        result = sell_product_service(product_id, quantity)
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@is_admin
def update_stock_controller(product_id):
    """
    Controller to update product stock.
    """
    try:
        data = request.get_json()
        new_stock = data.get("stock", None)

        if new_stock is None or new_stock < 0:
            return jsonify({"error": "Invalid stock value"}), 400

        result = update_stock_service(product_id, new_stock)
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@is_admin
def update_price_controller(product_id):
    """
    Controller to update product price.
    """
    try:
        data = request.get_json()
        new_price = data.get("price", None)

        if new_price is None or new_price < 0:
            return jsonify({"error": "Invalid price value"}), 400

        result = update_price_service(product_id, new_price)
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400
