# -*- coding: utf-8 -*-
"""Page Object da listagem de produtos e do detalhe."""

from .base_page import BasePage

ORDENACOES = {
    "Name (A to Z)": "az",
    "Name (Z to A)": "za",
    "Price (low to high)": "lohi",
    "Price (high to low)": "hilo",
}


class ProdutosPage(BasePage):
    ITEM = ".inventory_item"
    NOME = ".inventory_item_name"
    PRECO = ".inventory_item_price"
    IMAGEM = ".inventory_item_img img"
    SELETOR_ORDENACAO = '[data-test="product-sort-container"]'
    BADGE_CARRINHO = ".shopping_cart_badge"

    # detalhe do produto
    DETALHE_NOME = ".inventory_details_name"
    DETALHE_DESCRICAO = ".inventory_details_desc"
    DETALHE_PRECO = ".inventory_details_price"
    BOTAO_VOLTAR = "#back-to-products"

    def abrir(self, caminho: str = "/inventory.html") -> None:
        super().abrir(caminho)

    def aguardar_listagem(self, timeout: int = 15000) -> None:
        """Espera o primeiro produto aparecer.

        `locator.count()` não espera por nada: o Playwright só aguarda
        automaticamente em ações e em `expect`. Sem esta espera, a contagem
        roda antes da renderização em máquinas lentas (foi o que quebrou no CI
        e passava localmente).
        """
        self.page.locator(self.ITEM).first.wait_for(state="visible", timeout=timeout)

    def quantidade_de_produtos(self) -> int:
        self.aguardar_listagem()
        return self.page.locator(self.ITEM).count()

    def nomes(self) -> list[str]:
        return self.page.locator(self.NOME).all_inner_texts()

    def precos(self) -> list[float]:
        brutos = self.page.locator(self.PRECO).all_inner_texts()
        return [float(p.replace("$", "").strip()) for p in brutos]

    def todos_tem_imagem(self) -> bool:
        return self.page.locator(self.IMAGEM).count() == self.quantidade_de_produtos()

    def ordenar_por(self, rotulo: str) -> None:
        self.page.select_option(self.SELETOR_ORDENACAO, ORDENACOES[rotulo])

    def abrir_detalhe(self, nome: str) -> None:
        self.page.click(f"{self.NOME}:text-is('{nome}')")

    def _cartao_do_produto(self, nome: str):
        return self.page.locator(self.ITEM).filter(has_text=nome)

    def adicionar_ao_carrinho(self, nome: str) -> None:
        self._cartao_do_produto(nome).get_by_role("button", name="Add to cart").click()

    def remover_do_carrinho(self, nome: str) -> None:
        self._cartao_do_produto(nome).get_by_role("button", name="Remove").click()

    def rotulo_do_botao(self, nome: str) -> str:
        return self._cartao_do_produto(nome).locator("button").inner_text()

    def contador_do_carrinho(self) -> int:
        badge = self.page.locator(self.BADGE_CARRINHO)
        return int(badge.inner_text()) if badge.count() else 0

    # ------------------------------------------------------------- detalhe
    def detalhe_nome(self) -> str:
        return self.page.inner_text(self.DETALHE_NOME)

    def detalhe_descricao(self) -> str:
        return self.page.inner_text(self.DETALHE_DESCRICAO)

    def detalhe_preco(self) -> str:
        return self.page.inner_text(self.DETALHE_PRECO)

    def botao_visivel(self, rotulo: str) -> bool:
        return self.page.get_by_role("button", name=rotulo).is_visible()
