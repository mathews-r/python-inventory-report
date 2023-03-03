from datetime import datetime


class SimpleReport:
    @classmethod
    def generate(cls, data):
        return (
            f"Data de fabricação mais antiga: {cls.get_data_fabri(data)}\n"
            f"Data de validade mais próxima: {cls.get_data_validade(data)}\n"
            f"Empresa com mais produtos: {cls.get_nome_empresa(data)[-1][0]}"
        )

    @classmethod
    def get_data_fabri(cls, data):
        data_fabricacao = []
        for fabricacao in data:
            data_fabricacao.append(fabricacao["data_de_fabricacao"])
        return min(data_fabricacao)

    @classmethod
    def get_data_validade(cls, data):
        data_validade = []
        for fabricacao in data:
            if fabricacao["data_de_validade"] > str(datetime.today().date()):
                data_validade.append(fabricacao["data_de_validade"])
        return min(data_validade)

    @classmethod
    def get_nome_empresa(cls, data):
        empresas_dict = {}
        for empresa in data:
            if empresa["nome_da_empresa"] in empresas_dict:
                empresas_dict[empresa["nome_da_empresa"]] += 1
            else:
                empresas_dict[empresa["nome_da_empresa"]] = 1
        return sorted(empresas_dict.items(), key=lambda item: item[1])
