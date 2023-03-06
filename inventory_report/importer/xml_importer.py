from inventory_report.inventory.inventory import Importer
import xmltodict


class XmlImporter(Importer):
    @classmethod
    def read(cls, path):
        data = open(path, "r")
        xml_content = data.read()
        xml_ordered_dict = xmltodict.parse(xml_content)

        return xml_ordered_dict["dataset"]["record"]
