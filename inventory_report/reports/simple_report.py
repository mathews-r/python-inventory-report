from datetime import datetime


class SimpleReport:
    @classmethod
    def generate(cls, data):
        return (
            f"Data de fabricação mais antiga: {cls.get_data_fabricacao(data)}"
            f"Data de validade mais próxima: {cls.get_data_validade(data)}"
            f"Empresa com mais produtos: {cls.get_nome_empresa(data)}"
        )

    @classmethod
    def get_data_fabricacao(cls, data):
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
        empresas_dict = {"nome_da_empresa": "", "contador": 0}
        for empresa in data:
            print(empresas_dict)
            if empresa["nome_da_empresa"] == empresas_dict["nome_da_empresa"]:
                empresas_dict["contador"] += 1
            else:
                empresas_dict["nome_da_empresa"] = empresa["nome_da_empresa"]
                empresas_dict["contador"] = 0
        return empresas_dict["nome_da_empresa"]

    # @classmethod
    # def get_contador(e):
    #     return e["contador"]

    # nome_empresa = [{"nome": "", "contador": 0}].sort(key=cls.get_contador)
