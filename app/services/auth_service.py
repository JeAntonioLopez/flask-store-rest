from app.models import User
from app import db
import jwt
import datetime
import os

jwt_key = os.getenv("JWT_KEY")

def login_service(username, password):
    """
    Service for user login.
    """
    user = User.query.filter_by(username=username).first()
    if not user or (user.password != password):
        raise Exception("Invalid username or password")
    
    token = jwt.encode({
        "username": user.username,
        "user_type": user.type.value,  
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)
    }, jwt_key, algorithm="HS256")
    
    return token


def change_password_service(username, current_password, new_password, confirm_new_password):
    """
    Service for changing user password.
    """
    if new_password != confirm_new_password:
        raise Exception("New password and confirmation do not match")
    user = User.query.filter_by(username=username).first()
    if not user or (user.password != current_password):
        raise Exception("Invalid username or current password")
    user.password = new_password
    db.session.commit()
    return "Password updated successfully"
