from tinydb import TinyDB, Query
from tinydb.storages import MemoryStorage
from datetime import datetime

db = TinyDB('app/data/db.json')

class Workload:
    def __init__(self):
        self.table = db.table('workloads')

    def insert(self, workload):
        self.table.insert(workload)

    def get(self, workload_id: int):
        query = Query()
        return self.table.get(query.id == workload_id)

    def update(self, workload_id: int, update_data):
        query = Query()
        self.table.update(update_data, query.id == workload_id)

    def delete(self, workload_id: int):
        query = Query()
        self.table.remove(query.id == workload_id)

    def get_all(self):
        return self.table.all()
