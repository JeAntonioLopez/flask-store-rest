from flask import Blueprint
from app.controllers.product_controller import get_products_by_category_controller, get_all_categories_controller, sell_product_controller, update_stock_controller, update_price_controller

product_bp = Blueprint('product', __name__, url_prefix="/products")


@product_bp.route('/category/<int:category_id>', methods=['GET'])
def get_products_by_category(category_id):
    return get_products_by_category_controller(category_id)


@product_bp.route('/categories', methods=['GET'])
def get_all_categories():
    return get_all_categories_controller()


@product_bp.route("/<int:product_id>/sell", methods=["PATCH"])
def sell_product(product_id):
    return sell_product_controller(product_id)

@product_bp.route("/<int:product_id>/stock", methods=["PATCH"])
def update_stock(product_id):
    return update_stock_controller(product_id)

@product_bp.route("/<int:product_id>/price", methods=["PATCH"])
def update_price(product_id):
    return update_price_controller(product_id)
