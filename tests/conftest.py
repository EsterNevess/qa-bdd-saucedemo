# -*- coding: utf-8 -*-
"""Fixtures compartilhadas e captura de evidência em caso de falha."""

from pathlib import Path

import allure
import pytest
from playwright.sync_api import Page

from pages.login_page import LoginPage
from pages.produtos_page import ProdutosPage

EVIDENCIAS = Path(__file__).resolve().parents[1] / "evidencias"


@pytest.fixture
def login(page: Page) -> LoginPage:
    return LoginPage(page)


@pytest.fixture
def produtos(page: Page) -> ProdutosPage:
    return ProdutosPage(page)


@pytest.fixture
def contexto() -> dict:
    """Espaço para os steps trocarem dados dentro de um cenário."""
    return {}


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Em caso de falha, salva o print em disco e anexa ao relatório Allure.

    O arquivo em `evidencias/` serve para quem roda localmente; o anexo no
    Allure serve para quem só vai ver o relatório publicado. Um print que
    ninguém encontra não é evidência.
    """
    resultado = yield
    relatorio = resultado.get_result()
    if relatorio.when != "call" or not relatorio.failed:
        return

    page = item.funcargs.get("page")
    if page is None:
        return

    EVIDENCIAS.mkdir(exist_ok=True)
    destino = EVIDENCIAS / f"{item.name}.png"

    try:
        imagem = page.screenshot(path=str(destino), full_page=True)
        allure.attach(
            imagem,
            name=f"Tela no momento da falha - {item.name}",
            attachment_type=allure.attachment_type.PNG,
        )
        allure.attach(
            page.url,
            name="URL no momento da falha",
            attachment_type=allure.attachment_type.TEXT,
        )
        allure.attach(
            page.content(),
            name="HTML da página",
            attachment_type=allure.attachment_type.HTML,
        )
        print(f"\nEvidência salva em: {destino}")
    except Exception as erro:  # noqa: BLE001
        print(f"\nNão foi possível capturar a evidência: {erro}")
