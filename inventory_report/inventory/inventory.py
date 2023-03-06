from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv
import json
import xml.etree.ElementTree as ET


class Inventory:
    @classmethod
    def import_data(cls, path, type):
        report = ""
        if ".csv" in path:
            report = cls.read_csv(path)
        elif ".json" in path:
            report = cls.read_json(path)
        else:
            report = cls.read_xml(path)

        return cls.report_simple_or_complete(report, type)

    @classmethod
    def read_csv(cls, path):
        with open(path, mode="r") as file:
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
        data = ET.parse(path).getroot()

        print(ET.tostring(data))

    @classmethod
    def report_simple_or_complete(cls, report, type):
        if type == "simples":
            return SimpleReport.generate(report)
        else:
            return CompleteReport.generate(report)
