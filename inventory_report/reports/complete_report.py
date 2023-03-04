from inventory_report.reports.simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, data):
        return (
            f"{super().generate(data)}\n"
            f"Produtos estocados por empresa:\n"
            f"{cls.get_companies_by_products(data)}"
        )

    @classmethod
    def get_companies_by_products(cls, data):
        companies_list = []
        products_quantity = ""

        for company_name in data:
            companies_list.append(company_name["nome_da_empresa"])

        products = Counter(companies_list)
        for company in companies_list:
            products_quantity += f"- {company}: {products[company]}\n"
        return products_quantity
