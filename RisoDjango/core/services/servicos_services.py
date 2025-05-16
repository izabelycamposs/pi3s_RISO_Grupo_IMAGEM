from .db_connection import get_db

def service_exists(codigo):
    db = get_db()
    service = db["servicos"].find_one({"codigo": codigo})
    return service is not None

def register_service(service_data):
    db = get_db()
    
    if not service_exists(service_data.get("codigo")):
        codigo = service_data.get("codigo")
        tipo = service_data.get("tipo", "padrão")
        descricao = service_data.get("descricao", "")
        preco = service_data.get("preco", 0.0)
        duracao = service_data.get("duracao", 0)
        status = service_data.get("status", "ativo")
        quantidadeRodas = service_data.get("quantidadeRodas", 1)
        prazo = service_data.get("prazo", 0)

        service = {
            "codigo": codigo,
            "tipo": tipo,
            "descricao": descricao,
            "preco": preco,
            "prazo": prazo,
            "quantidadeRodas": quantidadeRodas,
            "status": status,
            "duracao": duracao
        }

        db["servicos"].insert_one(service)
        return True
    return False

def get_service(codigo):
    db = get_db()
    service = db["servicos"].find_one({"codigo": codigo})
    return service if service else None

def update_service(codigo, new_data):
    db = get_db()
    update_fields = {}
    if not service_exists(codigo):
        return False
    if "tipo" in new_data:
        update_fields["tipo"] = new_data["tipo"]
    if "descricao" in new_data:
        update_fields["descricao"] = new_data["descricao"]
    if "preco" in new_data:
        update_fields["preco"] = new_data["preco"]
    if "prazo" in new_data:
        update_fields["prazo"] = new_data["prazo"]
    if "quantidadeRodas" in new_data:
        update_fields["quantidadeRodas"] = new_data["quantidadeRodas"]
    if "duracao" in new_data:
        update_fields["duracao"] = new_data["duracao"]
    result = db["servicos"].update_one({"codigo": codigo}, {"$set": update_fields})
    return result.modified_count > 0

def delete_service(codigo):
    db = get_db()
    result = db["servicos"].delete_one({"codigo": codigo})
    return result.deleted_count > 0

def show_services():
    db = get_db()
    services = db["servicos"].find({})
    return list(services)

def count_services():
    db = get_db()
    return db["servicos"].count_documents({})

def get_active_services():
    db = get_db()
    active_services = db["servicos"].find({"status": "ativo"})
    return list(active_services)

def get_inactive_services():
    db = get_db()
    inactive_services = db["servicos"].find({"status": "inativo"})
    return list(inactive_services)

def get_service_by_type(tipo):
    db = get_db()
    service = db["servicos"].find_one({"tipo": tipo})
    return service if service else None






