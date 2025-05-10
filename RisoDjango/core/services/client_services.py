import bcrypt
from .db_connection import get_db

def create_client(data):
    db = get_db()
    
    if(get_client(data.get("documento"))):
        return False
    
    name = data.get("nome")
    document = data.get("documento")
    cep = data.get("cep")
    email = data.get("email")
    phone = data.get("telefone")
    home_phone = data.get("telefone_residencial")

    if not name or not document or not cep or not email:
        return False
    
    client = {
        "nome": name,
        "documento": document,
        "cep": cep,
        "email": email,
        "telefone": phone,
        "telefone_residencial": home_phone
    }
    print('---------------------------------')
    print(client)
    print('---------------------------------')
    
    print(db["clients"].insert_one(client))
    return True

def get_client(document):
    db = get_db()
    client = db["clients"].find_one({"documento": document})
    return client if client else None