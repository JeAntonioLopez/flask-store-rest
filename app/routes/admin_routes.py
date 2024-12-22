from flask import Blueprint
from app.controllers.admin_controller import (
    get_all_users_controller,
    create_vendor_controller,
    delete_vendor_controller
)

admin_bp = Blueprint('admin', __name__, url_prefix="/admin")

@admin_bp.route('/users', methods=['GET'])
def get_all_users():
    return get_all_users_controller()


@admin_bp.route('/users/vendor', methods=['POST'])
def create_vendor():
    return create_vendor_controller()

# Asegúrate de pasar el vendor_id en la URL para la eliminación
@admin_bp.route('/users/vendor/<int:vendor_id>', methods=['DELETE'])
def delete_vendor(vendor_id):
    return delete_vendor_controller(vendor_id)
