from inventory_report.reports.colored_report import ColoredReport
from inventory_report.reports.simple_report import SimpleReport


def test_decorar_relatorio():
    colored_report = ColoredReport(SimpleReport)

    expect = colored_report.generate(
        [
            {
                "id": 1,
                "nome_do_produto": "Vasco",
                "nome_da_empresa": "Vasco da Gama",
                "data_de_fabricacao": "2023-03-07",
                "data_de_validade": "2023-04-07",
                "numero_de_serie": "Vasco123",
                "instrucoes_de_armazenamento": "Vasco",
            }
        ]
    )

    response = """\033[32mData de fabricação mais antiga:\033[0m \033[36m2023-03-07\033[0m
\033[32mData de validade mais próxima:\033[0m \033[36m2023-04-07\033[0m
\033[32mEmpresa com mais produtos:\033[0m \033[31mVasco da Gama\033[0m"""

    assert expect == response
