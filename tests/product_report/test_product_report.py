from inventory_report.inventory.product import Product


def test_relatorio_produto():
    product = Product(
        1,
        "Teste",
        "QA",
        "10/03/2022",
        "15/03/2023",
        "123456",
        "Armazenar na luz",
    )

    assert str(product) == (
        f"O produto {product.nome_do_produto}"
        f" fabricado em {product.data_de_fabricacao}"
        f" por {product. nome_da_empresa} com validade"
        f" até {product.data_de_validade}"
        f" precisa ser armazenado {product.instrucoes_de_armazenamento}."
    )
