from inventory_report.reports.colored_report import ColoredReport
from inventory_report.reports.simple_report import SimpleReport


def test_decorar_relatorio():
    colored_report = ColoredReport(SimpleReport)

    colored_report.generate(
        [
            {
                "id": 1,
                "nome_do_produto": "Teste",
                "nome_da_empresa": "Teste SA",
                "data_de_fabricacao": "2023-03-07",
                "data_de_validade": "2023-04-07",
                "numero_de_serie": "TESTE123",
                "instrucoes_de_armazenamento": "Armazenar",
            }
        ]
    )
