import unittest
import os
from core.services.client_services import get_db 
from core.services.client_services import (
    replace_special_characters,
    validate_client_data,
    create_client,
    get_client,
    update_client,
    delete_client,
    list_clients,
    count_clients,
    client_exists
)

class ClientTestCase(unittest.TestCase):
    def setUp(self):
        os.environ["MONGO_DB_NAME"] = "testMongo"
        self.db = get_db()
        self.db["clients"].delete_many({})

        self.client_data = {
            "nome": "João Silva",
            "documento": "123.456.789-00",
            "cep": "13500-000",
            "email": "joao@teste.com",
            "telefone": "(11)99999-9999",
            "telefone_residencial": "(11)3333-3333"
        }
        create_client(self.client_data)

    def tearDown(self):
        self.db["clients"].delete_many({}) 

    def test_assert_db_usage(self):
        db = get_db()
        self.assertEqual(db.name, os.environ["MONGO_DB_NAME"])

    def test_replace_special_characters(self):
        self.assertEqual(replace_special_characters("123.456-789"), "123456789")

    def test_validate_client_data_valid(self):
        valid_data = {
            "nome": "Maria",
            "documento": "987.624.321-00",
            "cep": "12345-678",
            "email": "bla@bla.com",
            "telefone": "(11)99999-9999",
            "telefone_residencial": "(11)3333-3333"
        }
        try:
            validate_client_data(valid_data)
        except Exception as e:
            self.fail(f"Erro inesperado: {e}")

    def test_create_client_success(self):
        self.client_data["documento"] = "987.654.321-00"
        result = create_client(self.client_data)
        self.assertTrue(result)
        self.assertEqual(self.db["clients"].count_documents({}), 2)

    def test_create_client_duplicate_document(self):
        with self.assertRaises(ValueError):
            create_client(self.client_data)

    def test_get_client_found(self):
        result = get_client(self.client_data["documento"])
        self.assertIsNotNone(result)
        self.assertEqual(result["nome"], "João Silva")

    def test_get_client_not_found(self):
        result = get_client("000.000.000-00")
        self.assertIsNone(result)

    def test_update_client_success(self):
        new_email = "novo@teste.com"
        updated = update_client(self.client_data["documento"], {"email": new_email})
        self.assertTrue(updated)
        updated_data = get_client(self.client_data["documento"])
        self.assertEqual(updated_data["email"], new_email)

    def test_update_client_not_found(self):
        result = update_client("000.000.000-00", {"email": "x@x.com"})
        self.assertFalse(result)

    def test_delete_client_not_found(self):
        result = delete_client("000.000.000-00")
        self.assertFalse(result)

    def test_list_clients(self):
        clients = list_clients()
        self.assertEqual(len(clients), 1)
        self.assertEqual(clients[0]["nome"], self.client_data["nome"])

    def test_count_clients(self):
        self.assertEqual(count_clients(), 1)

    def test_client_exists_true(self):
        exists = client_exists(self.client_data["documento"])
        self.assertTrue(exists)

    def test_client_exists_false(self):
        exists = client_exists("000.000.000-00")
        self.assertFalse(exists)

    def test_delete_client_success(self):
        deleted = delete_client(self.client_data["documento"])
        self.assertTrue(deleted)
        self.assertEqual(self.db["clients"].count_documents({}), 0)
if __name__ == "__main__":
    unittest.main()
    