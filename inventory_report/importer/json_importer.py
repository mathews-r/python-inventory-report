from inventory_report.inventory.inventory import Importer
import json


class JsonImporter(Importer):
    @classmethod
    def read(cls, path):
        with open(path, mode="r") as file:
            data = json.load(file)
        return data
