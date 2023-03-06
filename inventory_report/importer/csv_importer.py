from inventory_report.importer.importer import Importer
import csv


class CsvImporter(Importer):
    @classmethod
    def import_data(cls, path):
        if path.endswith(".csv"):
            with open(path, mode="r") as file:
                data = csv.DictReader(file, delimiter=",")
                data_list = []
                for data_csv in data:
                    data_list.append(data_csv)
            return data_list

        raise ValueError('Arquivo inválido')
