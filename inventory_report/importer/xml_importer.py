from inventory_report.importer.importer import Importer
import xmltodict


class XmlImporter(Importer):
    @classmethod
    def import_data(cls, path):
        if path.endswith(".xml"):
            data = open(path, "r")
            xml_content = data.read()
            xml_ordered_dict = xmltodict.parse(xml_content)

            return xml_ordered_dict["dataset"]["record"]

        raise ValueError("Arquivo inválido")
