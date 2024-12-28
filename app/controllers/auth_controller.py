from flask import request, jsonify
from app.services.auth_service import login_service, change_password_service

def login_controller():
    """
    Controller for user login.
    """
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    try:
        token = login_service(username, password)
        return jsonify({"token": token}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

def change_password_controller():
    """
    Controller for changing user password.
    """
    data = request.get_json()
    username = data.get("username")
    current_password = data.get("currentPassword")
    new_password = data.get("newPassword")
    confirm_new_password = data.get("confirmNewPassword")
    try:
        message = change_password_service(username, current_password, new_password, confirm_new_password)
        return jsonify({"message": message}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400
