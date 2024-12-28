from functools import wraps
from flask import request, jsonify
import os
import jwt
from app.models import UserType

jwt_key = os.getenv("JWT_KEY")

def is_admin(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        auth_header = request.headers.get("Authorization")
        if not auth_header or not auth_header.startswith("Bearer "):
            return jsonify({"error": "Authorization token is missing or invalid"}), 401
        
        token = auth_header.split(" ")[1]
        try:
            payload = jwt.decode(token, jwt_key, algorithms=["HS256"])
            if payload.get("user_type") != UserType.ADMIN.value :
                return jsonify({"error": "Access denied: Admins only"}), 403
        except jwt.ExpiredSignatureError:
            return jsonify({"error": "Token has expired"}), 401
        except jwt.InvalidTokenError:
            return jsonify({"error": "Invalid token"}), 401
        
        return func(*args, **kwargs)
    return decorated_function

def can_sell(func):  
    @wraps(func)
    def decorated_function(*args, **kwargs):
        auth_header = request.headers.get("Authorization")
        if not auth_header or not auth_header.startswith("Bearer "):
            return jsonify({"error": "Authorization token is missing or invalid"}), 401
        
        token = auth_header.split(" ")[1]
        try:
            payload = jwt.decode(token, jwt_key, algorithms=["HS256"])
            if payload.get("user_type") not in [UserType.ADMIN.value , UserType.VENDOR.value ]:
                return jsonify({"error": "Access denied: Only admins or vendors"}), 403
        except jwt.ExpiredSignatureError:
            return jsonify({"error": "Token has expired"}), 401
        except jwt.InvalidTokenError:
            return jsonify({"error": "Invalid token"}), 401
        
        return func(*args, **kwargs)
    return decorated_function
