# -*- coding: utf-8 -*-
"""Steps dos cenários de carrinho (CT-G12 e CT-G13)."""

from pytest_bdd import given, parsers, scenarios, then, when

scenarios("../features/carrinho.feature")

SENHA_PADRAO = "secret_sauce"


@given(parsers.parse('que estou autenticado como "{usuario}"'))
def autenticado(login, usuario):
    login.autenticar(usuario, SENHA_PADRAO)


@given(parsers.parse('que tenho o produto "{nome}" no carrinho'), target_fixture="produto")
def produto_no_carrinho(produtos, nome):
    produtos.adicionar_ao_carrinho(nome)
    assert produtos.contador_do_carrinho() == 1, "Pré-condição falhou: carrinho vazio"
    return nome


@when(parsers.parse('adiciono o produto "{nome}" ao carrinho'), target_fixture="produto")
def adicionar(produtos, nome):
    produtos.adicionar_ao_carrinho(nome)
    return nome


@when(parsers.parse('removo o produto "{nome}" do carrinho'))
def remover(produtos, nome):
    produtos.remover_do_carrinho(nome)


@then(parsers.parse("o ícone do carrinho deve exibir {quantidade:d}"))
def contador_do_carrinho(produtos, quantidade):
    atual = produtos.contador_do_carrinho()
    assert atual == quantidade, f"Esperava {quantidade} no carrinho, veio {atual}"


@then("o ícone do carrinho não deve exibir contador")
def carrinho_sem_contador(produtos):
    atual = produtos.contador_do_carrinho()
    assert atual == 0, f"O carrinho ainda exibe {atual}"


@then(parsers.parse('o botão do produto deve mudar para "{rotulo}"'))
def rotulo_do_botao(produtos, produto, rotulo):
    atual = produtos.rotulo_do_botao(produto).strip()
    assert atual.lower() == rotulo.lower(), f"Esperava {rotulo!r}, veio {atual!r}"
