from .db_connection import get_db

def create_client(data):
    db = get_db()
    
    name = data.get("nome")
    document = data.get("documento")
    cep = data.get("cep")
    email = data.get("email")
    phone = data.get("telefone")
    home_phone = data.get("telefone_residencial")

    if client_exists(document):
        return False

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
    
    print(db["clients"].insert_one(client))
    return True

def get_client(document):
    db = get_db()
    client = db["clients"].find_one({"documento": document})
    return client if client else None

def update_client(document, new_data):
    db = get_db()
    update_fields = {}

    if not get_client(document):
        return False
    
    if "nome" in new_data:
        update_fields["nome"] = new_data["nome"]
    if "cep" in new_data:
        update_fields["cep"] = new_data["cep"]
    if "email" in new_data:
        update_fields["email"] = new_data["email"]
    if "telefone" in new_data:
        update_fields["telefone"] = new_data["telefone"]
    if "telefone_residencial" in new_data:
        update_fields["telefone_residencial"] = new_data["telefone_residencial"]

    result = db["clients"].update_one({"documento": document}, {"$set": update_fields})
    return result.modified_count > 0

def delete_client(document):
    db = get_db()
    result = db["clients"].delete_one({"documento": document})
    return result.deleted_count > 0

def list_clients():
    db = get_db()
    clients = db["clients"].find({})
    return list(clients)

def count_clients():
    db = get_db()
    return db["clients"].count_documents({})

def client_exists(document):
    db = get_db()
    client = db["clients"].find_one({"documento": document})
    return client is not None