from datetime import datetime


class SimpleReport:
    @classmethod
    def generate(cls, data):
        return (
            f"Data de fabricação mais antiga: {cls.get_manufac_date(data)}\n"
            f"Data de validade mais próxima: {cls.get_expiration_date(data)}\n"
            f"Empresa com mais produtos: {cls.get_company_name(data)[-1][0]}"
        )

    @classmethod
    def get_manufac_date(cls, data):
        manufacturing_date = []
        for manufacturing in data:
            manufacturing_date.append(manufacturing["data_de_fabricacao"])
        return min(manufacturing_date)

    @classmethod
    def get_expiration_date(cls, data):
        expiration_date = []
        for manufact in data:
            if manufact["data_de_validade"] > str(datetime.today().date()):
                expiration_date.append(manufact["data_de_validade"])
        return min(expiration_date)

    @classmethod
    def get_company_name(cls, data):
        companies_dict = {}
        for company in data:
            if company["nome_da_empresa"] in companies_dict:
                companies_dict[company["nome_da_empresa"]] += 1
            else:
                companies_dict[company["nome_da_empresa"]] = 1
        return sorted(companies_dict.items(), key=lambda item: item[1])
