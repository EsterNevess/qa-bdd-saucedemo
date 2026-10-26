# -*- coding: utf-8 -*-
"""Base comum aos Page Objects."""

from playwright.sync_api import Page

URL_BASE = "https://www.saucedemo.com"


class BasePage:
    """Guarda a página do Playwright e o endereço base."""

    def __init__(self, page: Page) -> None:
        self.page = page

    def abrir(self, caminho: str = "/") -> None:
        self.page.goto(f"{URL_BASE}{caminho}")

    @property
    def url_atual(self) -> str:
        return self.page.url
