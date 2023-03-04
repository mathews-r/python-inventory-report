from inventory_report.reports.simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, data):
        return (
            f"{super().generate(data)}\n"
            f"Produtos estocados por empresa:\n"
            f"{cls.get_produtos_por_empresa(data)}"
        )

    @classmethod
    def get_produtos_por_empresa(cls, data):
        lista_empresas = []
        quant_produtos = ""

        for nome in data:
            lista_empresas.append(nome["nome_da_empresa"])

        products = Counter(lista_empresas)
        for empresa in lista_empresas:
            quant_produtos += f"- {empresa}: {products[empresa]}\n"
        return quant_produtos
