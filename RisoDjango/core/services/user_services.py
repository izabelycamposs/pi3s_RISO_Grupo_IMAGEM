import bcrypt
from .db_connection import get_db

def verify_user(username):
    db = get_db()
    user = db["users"].find_one({"username": username})
    return user is not None 

def create_user(username, password):
    db = get_db()
    if not verify_user(username):
        hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        user = {
            "username": username,
            "password": hashed
        }
        db["users"].insert_one(user)
        return True
    return False

def auth_user(username, password):
    db = get_db()
    user = db["users"].find_one({"username": username})
    if user and bcrypt.checkpw(password.encode('utf-8'), user["password"]):
        return True
    return False

def auth_session(session):
    if (not session.get('session', False) or
        not session.get('username', None)):
        return False
    if session.get('session') != 'active':
        return False
    return True
    

def get_user(username):
    db = get_db()
    user = db["users"].find_one({"username": username})
    return user if user else None

def update_user(username, new_data):
    db = get_db()

    if "password" in new_data:
        new_data["password"] = bcrypt.hashpw(new_data["password"].encode('utf-8'), bcrypt.gensalt())

    result = db["users"].update_one({"username": username}, {"$set": new_data})
    return result.modified_count > 0

def delete_user(username):
    db = get_db()
    result = db["users"].delete_one({"username": username})
    return result.deleted_count > 0

def show_users():
    db = get_db()
    usuarios = db["users"].find({}, {"password": 0})  # Oculta senhas
    return list(usuarios)

def count_users():
    db = get_db()
    return db["users"].count_documents({})
