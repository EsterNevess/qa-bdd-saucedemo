# language: pt
Funcionalidade: Carrinho de compras
  Como usuário autenticado
  Quero adicionar e remover produtos do carrinho
  Para montar o meu pedido

  Contexto:
    Dado que estou autenticado como "standard_user"

  Cenário: CT-G12 - Adicionar produto ao carrinho
    Quando adiciono o produto "Sauce Labs Backpack" ao carrinho
    Então o ícone do carrinho deve exibir 1
    E o botão do produto deve mudar para "Remove"

  Cenário: CT-G13 - Remover produto do carrinho
    Dado que tenho o produto "Sauce Labs Backpack" no carrinho
    Quando removo o produto "Sauce Labs Backpack" do carrinho
    Então o ícone do carrinho não deve exibir contador
    E o botão do produto deve mudar para "Add to cart"
