# -*- coding: utf-8 -*-
"""Steps dos cenários de catálogo (CT-G06 a CT-G11)."""

from pytest_bdd import given, parsers, scenarios, then, when

scenarios("../features/produtos.feature")

SENHA_PADRAO = "secret_sauce"


@given(parsers.parse('que estou autenticado como "{usuario}"'))
def autenticado(login, usuario):
    login.autenticar(usuario, SENHA_PADRAO)


@when("acesso a página de produtos")
def acessar_produtos(produtos):
    produtos.abrir()


@when(parsers.parse('seleciono a ordenação "{rotulo}"'))
def ordenar(produtos, rotulo):
    produtos.ordenar_por(rotulo)


@when(parsers.parse('abro os detalhes do produto "{nome}"'))
def abrir_detalhe(produtos, nome):
    produtos.abrir_detalhe(nome)


@then(parsers.parse("devo visualizar {quantidade:d} produtos listados"))
def quantidade_de_produtos(produtos, quantidade):
    encontrados = produtos.quantidade_de_produtos()
    assert encontrados == quantidade, (
        f"Esperava {quantidade} produtos, encontrei {encontrados}"
    )


@then("cada produto deve exibir nome, preço e imagem")
def produto_completo(produtos):
    total = produtos.quantidade_de_produtos()
    assert len(produtos.nomes()) == total, "Há produto sem nome"
    assert len(produtos.precos()) == total, "Há produto sem preço"
    assert produtos.todos_tem_imagem(), "Há produto sem imagem"


@then("os preços devem estar em ordem crescente")
def precos_crescentes(produtos):
    precos = produtos.precos()
    assert precos == sorted(precos), f"Preços fora de ordem: {precos}"


@then("os preços devem estar em ordem decrescente")
def precos_decrescentes(produtos):
    precos = produtos.precos()
    assert precos == sorted(precos, reverse=True), f"Preços fora de ordem: {precos}"


@then(parsers.parse("o primeiro produto deve custar {valor:f}"))
def primeiro_preco(produtos, valor):
    primeiro = produtos.precos()[0]
    assert primeiro == valor, f"Esperava {valor}, veio {primeiro}"


@then("os nomes devem estar em ordem alfabética crescente")
def nomes_crescentes(produtos):
    nomes = produtos.nomes()
    assert nomes == sorted(nomes), f"Nomes fora de ordem: {nomes}"


@then("os nomes devem estar em ordem alfabética decrescente")
def nomes_decrescentes(produtos):
    nomes = produtos.nomes()
    assert nomes == sorted(nomes, reverse=True), f"Nomes fora de ordem: {nomes}"


@then(parsers.parse('o primeiro produto deve ser "{nome}"'))
def primeiro_nome(produtos, nome):
    primeiro = produtos.nomes()[0]
    assert primeiro == nome, f"Esperava {nome!r}, veio {primeiro!r}"


@then("o nome, a descrição e o preço devem ser exibidos")
def detalhe_completo(produtos):
    assert produtos.detalhe_nome().strip(), "Nome do produto vazio"
    assert produtos.detalhe_descricao().strip(), "Descrição do produto vazia"
    assert produtos.detalhe_preco().strip().startswith("$"), "Preço do produto inválido"


@then(parsers.parse('o botão "{rotulo}" deve estar disponível'))
def botao_disponivel(produtos, rotulo):
    assert produtos.botao_visivel(rotulo), f"O botão {rotulo!r} não está visível"
