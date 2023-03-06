from inventory_report.reports.simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, data):
        return (
            f"{super().generate(data)}\n"
            f"Produtos estocados por empresa:\n"
            f"{cls.get_products_by_companies(data)}"
        )

    @classmethod
    def get_companies(cls, data):
        companies_list = []

        for company_name in data:
            companies_list.append(company_name["nome_da_empresa"])
        return companies_list

    @classmethod
    def get_products_by_companies(cls, data):
        products_quantity = ""
        companies_list = cls.get_companies(data)

        products = Counter(companies_list).items()
        for company, quantity in products:
            products_quantity += f"- {company}: {quantity}\n"
        return products_quantity
