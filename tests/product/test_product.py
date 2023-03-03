from inventory_report.inventory.product import Product


def test_cria_produto():
    product = Product(
        1,
        "Produto",
        "Empresa",
        "03/03/2023",
        "04/03/2023",
        "123456",
        "Armazenar",
    )

    assert product.id == 1
    assert product.nome_do_produto == "Produto"
    assert product.nome_da_empresa == "Empresa"
    assert product.data_de_fabricacao == "03/03/2023"
    assert product.data_de_validade == "04/03/2023"
    assert product.numero_de_serie == "123456"
    assert product.instrucoes_de_armazenamento == "Armazenar"
