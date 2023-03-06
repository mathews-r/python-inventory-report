from inventory_report.importer.importer import Importer
import json


class JsonImporter(Importer):
    @classmethod
    def import_data(cls, path):
        if path.endswith(".json"):
            with open(path, mode="r") as file:
                return json.load(file)

        raise ValueError("Arquivo inválido")


# formas de identificar o final do arquivo
# file_ext = path[path.rfind(".")]
# path[-1:-4]
# path.endswith(".json")
