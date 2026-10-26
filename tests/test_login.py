# -*- coding: utf-8 -*-
"""Steps dos cenários de login (CT-G01 a CT-G05)."""

from pytest_bdd import given, parsers, scenarios, then, when

scenarios("../features/login.feature")


@given("que acesso a página de login do Saucedemo")
def acessar_login(login):
    login.abrir()


@when(parsers.parse('preencho o campo Nome de usuário com "{usuario}"'))
def preencher_usuario(login, usuario):
    login.preencher_usuario(usuario)


@when(parsers.parse('preencho o campo Senha com "{senha}"'))
def preencher_senha(login, senha):
    login.preencher_senha(senha)


@when("deixo o campo Nome de usuário em branco")
def usuario_em_branco(login):
    login.preencher_usuario("")


@when("deixo o campo Senha em branco")
def senha_em_branco(login):
    login.preencher_senha("")


@when("clico no botão Login")
def clicar_login(login):
    login.entrar()


@then("devo ser redirecionado para a página de produtos")
def redirecionado_para_produtos(login):
    assert "/inventory.html" in login.url_atual, (
        f"Esperava a página de produtos, mas estou em {login.url_atual}"
    )


@then("devo visualizar a lista de produtos disponíveis")
def lista_visivel(produtos):
    assert produtos.quantidade_de_produtos() > 0, "Nenhum produto foi listado"


@then("devo permanecer na tela de login")
def permanece_no_login(login):
    assert "/inventory.html" not in login.url_atual, (
        "O login não deveria ter sido concluído"
    )


@then(parsers.parse('devo visualizar a mensagem de erro "{trecho}"'))
def mensagem_de_erro(login, trecho):
    assert login.erro_visivel(), "Nenhuma mensagem de erro foi exibida"
    assert trecho in login.mensagem_de_erro, (
        f"Esperava conter {trecho!r}, mas veio {login.mensagem_de_erro!r}"
    )
