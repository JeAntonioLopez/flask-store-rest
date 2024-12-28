from flask import Blueprint
from app.controllers.auth_controller import login_controller, change_password_controller

auth_bp = Blueprint('auth', __name__, url_prefix="/auth")

@auth_bp.route('/login', methods=['POST'])
def login():
    return login_controller()

@auth_bp.route('/change-password', methods=['PUT'])
def change_password():
    return change_password_controller()
