# app/services/admin_service.py
from app import db 
from app.models import User 
from app.models import UserType

def get_all_users_service():
    """
    Get all users.
    """
    try:
        users = User.query.all() 
        user_list = [{"id": u.id, "username": u.username, "type": u.type.value} for u in users]
        return user_list
    except Exception as e:
        raise Exception(f"Error al obtener los usuarios: {str(e)}")

def create_vendor_service(username, password):
    """
    Create a new vendor user.
    """
    try:
        if User.query.filter_by(username=username).first():
            raise Exception("Username already exists")

        vendor_user = User(username=username, password=password, type=UserType.VENDOR)
        db.session.add(vendor_user)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        raise Exception(f"Error creating vendor: {str(e)}")

def delete_vendor_service(vendor_id):
    """
    Delete a vendor user by id.
    """
    try:
        vendor_user = User.query.get(vendor_id)
        if not vendor_user or vendor_user.type != UserType.VENDOR:
            raise Exception("Vendor not found")

        db.session.delete(vendor_user)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        raise Exception(f"Error deleting vendor: {str(e)}")