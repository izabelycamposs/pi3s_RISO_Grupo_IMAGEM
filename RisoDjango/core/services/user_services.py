import bcrypt
from .db_connection import get_db

def verify_user(username):
    db = get_db()
    user = db["usuarios"].find_one({"username": username})
    return user is not None 

def create_user(username, password):
    db = get_db()
    if not usuario_existe(username):
        hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        user = {
            "username": username,
            "password": hashed
        }
        db["usuarios"].insert_one(user)
        return True
    return False

def auth_user(username, password):
    db = get_db()
    user = db["usuarios"].find_one({"username": username})
    if user and bcrypt.checkpw(password.encode('utf-8'), user["password"]):
        return True
    return False

def get_user(username):
    db = get_db()
    user = db["usuarios"].find_one({"username": username})
    return user if user else None

def update_user(username, new_data):
    db = get_db()

    if "password" in new_data:
        new_data["password"] = bcrypt.hashpw(new_data["password"].encode('utf-8'), bcrypt.gensalt())

    result = db["usuarios"].update_one({"username": username}, {"$set": new_data})
    return result.modified_count > 0

def delete_user(username):
    db = get_db()
    result = db["usuarios"].delete_one({"username": username})
    return result.deleted_count > 0

def show_users():
    db = get_db()
    usuarios = db["usuarios"].find({}, {"password": 0})  # Oculta senhas
    return list(usuarios)

def count_users():
    db = get_db()
    return db["usuarios"].count_documents({})
