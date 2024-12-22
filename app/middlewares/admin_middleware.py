from functools import wraps
from flask import request, jsonify


def is_admin(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        try:
            user = request.authorization["username"]
            password = request.authorization["password"]
        except TypeError:
            return jsonify({"error": "User didnt provide any credentials(basic auth)"}), 401

        if user == 'admin' and password == '123':
            return func(*args, **kwargs)
        return jsonify({"message": "Authorization failed"}), 401

    return decorated_function