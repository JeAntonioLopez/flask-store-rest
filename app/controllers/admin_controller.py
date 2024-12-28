# app/controllers/admin_controller.py

from flask import request, jsonify
from app.services.admin_service import get_all_users_service,  create_vendor_service, delete_vendor_service
from app.middlewares.middlewares import is_admin


@is_admin
def get_all_users_controller():
    """
    Controller to get all users.
    """
    try:
        users = get_all_users_service() 
        return jsonify({'users': users}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@is_admin
def create_vendor_controller():
    """
    Controller to create a new vendor.
    """
    try:
        data = request.get_json()
        username = data.get("username")
        password = data.get("password")

        if not username or not password:
            return jsonify({"error": "Missing username or password"}), 400

        create_vendor_service(username, password)
        return jsonify({"message": "Vendor created successfully"}), 201

    except Exception as e:
        print(e)
        return jsonify({"error": str(e)}), 500


@is_admin
def delete_vendor_controller(vendor_id):
    """
    Controller to delete a vendor.
    """
    try:
        delete_vendor_service(vendor_id)
        return jsonify({"message": "Vendor deleted successfully"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500
