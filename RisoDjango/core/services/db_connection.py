from pymongo import MongoClient

class MongoDBConnection:
    def __init__(self, ip='mongodb://localhost', port='27017', db_name='riso'):
        self.client = MongoClient(f"{ip}:{port}")
        self.db = self.client[db_name]

    def use_db(self, db_name):
        """Troca o banco de dados ativo."""
        self.db = self.client[db_name]

    def get_db(self):
        """Retorna o banco de dados atual."""
        return self.db
