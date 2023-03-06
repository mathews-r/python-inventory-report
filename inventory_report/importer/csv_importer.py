from inventory_report.inventory.inventory import Importer
import csv


class CsvImporter(Importer):
    @classmethod
    def read(cls, path):
        try:

            with open(path, mode="r") as file:
                data = csv.DictReader(file, delimiter=",")
                data_list = []
                for data_csv in data:
                    data_list.append(data_csv)
            return data_list
        except:
            raise ValueError
