from inventory_report.reports.simple_report import SimpleReport
import csv
import json
import xml.etree.ElementTree as Et


class Inventory:
    @classmethod
    def import_data(cls, path, type="completo"):
        report = ""
        report2 = ""
        if "csv" in path:
            report = cls.read_csv(path)
            report2 = SimpleReport.generate(report)
        elif "json" in path:
            report = cls.read_json(path)
            report2 = SimpleReport.generate(report)
        elif "xml" in path:
            report = cls.read_xml(path)
            report2 = SimpleReport.generate(report)

        return report2

    @classmethod
    def read_csv(cls, path):
        with open(path, mode="r", encoding="utf-8") as file:
            data = csv.DictReader(file, delimiter=",")
            data_list = []
            for data_csv in data:
                data_list.append(data_csv)

        return data_list

    @classmethod
    def read_json(cls, path):
        with open(path, mode="r") as file:
            data = json.load(file)
        return data

    @classmethod
    def read_xml(cls, path):
        with open(path, mode="r", encoding="utf-8") as file:
            xml = Et.parse(file)
        return xml
