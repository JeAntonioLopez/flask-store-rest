# app/controllers/admin_controller.py

from flask import request, jsonify
from app.services.admin_service import get_all_users_service,  create_vendor_service, delete_vendor_service
from app.middlewares.admin_middleware import is_admin


@is_admin
def get_all_users_controller():
    """
    Controlador para obtener todos los usuarios.
    Esta ruta está protegida para que solo los administradores puedan acceder.
    """
    try:
        users = get_all_users_service()  # Llamada al servicio
        return jsonify({'users': users}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@is_admin
def create_vendor_controller():
    """
    Controlador para crear un nuevo usuario de tipo Vendor.
    Solo accesible por administradores.
    """
    try:
        data = request.get_json()
        username = data.get("username")
        password = data.get("password")

        if not username or not password:
            return jsonify({"error": "Missing username or password"}), 400

        # Llamada al servicio para crear el usuario
        create_vendor_service(username, password)
        return jsonify({"message": "Vendor created successfully"}), 201

    except Exception as e:
        print(e)
        return jsonify({"error": str(e)}), 500


@is_admin
def delete_vendor_controller(vendor_id):
    """
    Controlador para eliminar un usuario Vendor.
    Solo accesible por administradores.
    """
    try:
        # Llamada al servicio para eliminar el usuario
        delete_vendor_service(vendor_id)
        return jsonify({"message": "Vendor deleted successfully"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500
