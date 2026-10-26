# -*- coding: utf-8 -*-
"""Page Object da tela de login."""

from .base_page import BasePage


class LoginPage(BasePage):
    CAMPO_USUARIO = "#user-name"
    CAMPO_SENHA = "#password"
    BOTAO_LOGIN = "#login-button"
    MENSAGEM_ERRO = '[data-test="error"]'

    def abrir(self, caminho: str = "/") -> None:
        super().abrir(caminho)

    def preencher_usuario(self, usuario: str) -> None:
        self.page.fill(self.CAMPO_USUARIO, usuario)

    def preencher_senha(self, senha: str) -> None:
        self.page.fill(self.CAMPO_SENHA, senha)

    def entrar(self) -> None:
        self.page.click(self.BOTAO_LOGIN)

    def autenticar(self, usuario: str, senha: str) -> None:
        self.abrir()
        self.preencher_usuario(usuario)
        self.preencher_senha(senha)
        self.entrar()

    @property
    def mensagem_de_erro(self) -> str:
        return self.page.inner_text(self.MENSAGEM_ERRO)

    def erro_visivel(self) -> bool:
        return self.page.is_visible(self.MENSAGEM_ERRO)
