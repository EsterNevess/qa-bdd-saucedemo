# -*- coding: utf-8 -*-
"""Fixtures compartilhadas e captura de evidência em caso de falha."""

from pathlib import Path

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
    """Salva um print da tela quando um cenário falha."""
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
        page.screenshot(path=str(destino), full_page=True)
        print(f"\nEvidência salva em: {destino}")
    except Exception as erro:  # noqa: BLE001
        print(f"\nNão foi possível capturar a evidência: {erro}")
