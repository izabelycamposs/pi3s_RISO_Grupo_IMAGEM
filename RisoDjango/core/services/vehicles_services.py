from .db_connection import get_db

def register_vehicle(vehicle_data):
    db = get_db()
    if not vehicle_exists(vehicle_data.get("placa")):
        tipo = vehicle_data.get("tipo", "carro")
        placa = vehicle_data.get("placa")
        marca = vehicle_data.get("marca")
        modelo = vehicle_data.get("modelo")
        ano = vehicle_data.get("ano")
        kilometragem = vehicle_data.get("quilometragem", 0)
        cor = vehicle_data.get("cor", "não especificada")
        observacoes = vehicle_data.get("observacoes", "")

        vehicle = {
            "tipo": tipo,
            "placa": placa,
            "marca": marca,
            "modelo": modelo,
            "ano": ano,
            "quilometragem": kilometragem,
            "cor": cor,
            "observacoes": observacoes
        }

        db["vehicles"].insert_one(vehicle)
        return True
    return False

def get_vehicle(placa):
    db = get_db()
    vehicle = db["vehicles"].find_one({"placa": placa})
    return vehicle if vehicle else None

def update_vehicle(placa, new_data):
    db = get_db()
    update_fields = {}

    if not vehicle_exists(placa):
        return False
    
    if "tipo" in new_data:
        update_fields["tipo"] = new_data["tipo"]
    if "marca" in new_data:
        update_fields["marca"] = new_data["marca"]
    if "modelo" in new_data:
        update_fields["modelo"] = new_data["modelo"]
    if "ano" in new_data:
        update_fields["ano"] = new_data["ano"]
    if "quilometragem" in new_data:
        update_fields["quilometragem"] = new_data["quilometragem"]
    if "cor" in new_data:
        update_fields["cor"] = new_data["cor"]
    if "observacoes" in new_data:
        update_fields["observacoes"] = new_data["observacoes"]

    result = db["vehicles"].update_one({"placa": placa}, {"$set": update_fields})
    return result.modified_count > 0

def delete_vehicle(placa):
    db = get_db()
    result = db["vehicles"].delete_one({"placa": placa})
    return result.deleted_count > 0

def list_vehicles():
    db = get_db()
    vehicles = db["vehicles"].find({})
    return list(vehicles)

def count_vehicles():
    db = get_db()
    return db["vehicles"].count_documents({})

def vehicle_exists(placa):
    db = get_db()
    return db["vehicles"].find_one({"placa": placa}) is not None
