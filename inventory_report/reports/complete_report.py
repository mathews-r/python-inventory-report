# from inventory_report.reports.simple_report import SimpleReport
from simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, data):
        return (
            f"{super().generate(data)}\n"
            f"Produtos estocados por empresa:\n"
            f"{cls.get_nome_empresa(data)}"
            # f"{cls.get_quant_produtos(data)}"
        )

    @classmethod
    def get_nome_empresa(cls, data):
        teste = super().get_nome_empresa(data)
        print(teste)

        for nome in teste:
            return f"- {nome[0]}: {nome[1]}"
        
        # return f"- {teste[0][0]}: {teste[0][1]}"

        # lista_empresa = []
        # nome_empresa = ""
        # for nome in data:
        #     if nome["nome_da_empresa"] not in lista_empresa:
        #         lista_empresa.append(nome["nome_da_empresa"])
        # for empresa in lista_empresa:
        #     if empresa not in nome_empresa:
        #         nome_empresa = empresa
        # print(f"- {lista_empresa}: 1")
        # return f"- {nome_empresa}: 1"

    @classmethod
    def get_quant_produtos(cls, data):
        dict_empresa_quanti = {}
        for produtos in data:
            if produtos["nome_do_produto"] in dict_empresa_quanti:
                dict_empresa_quanti[produtos["nome_do_produto"]] += 1
            else:
                dict_empresa_quanti[produtos["nome_do_produto"]] = 1
        # return dict_empresa_quanti


print(
    CompleteReport.get_nome_empresa(
        [
            {
                "id": 1,
                "nome_do_produto": "MESA",
                "nome_da_empresa": "Forces of Nature",
                "data_de_fabricacao": "2022-05-04",
                "data_de_validade": "2023-02-09",
                "numero_de_serie": "FR48",
                "instrucoes_de_armazenamento": "Conservar ao abrigo de luz",
            },
            {
                "id": 2,
                "nome_do_produto": "CADEIRA",
                "nome_da_empresa": "Teste",
                "data_de_fabricacao": "2022-05-04",
                "data_de_validade": "2023-02-09",
                "numero_de_serie": "FR48",
                "instrucoes_de_armazenamento": "Conservar ao abrigo SOL",
            },
            {
                "id": 2,
                "nome_do_produto": "FONE",
                "nome_da_empresa": "Bryant",
                "data_de_fabricacao": "2022-07-04",
                "data_de_validade": "2023-05-09",
                "numero_de_serie": "FR45",
                "instrucoes_de_armazenamento": "Conservar ao abrigo agua",
            },
        ]
    )
)
