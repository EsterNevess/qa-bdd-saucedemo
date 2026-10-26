# language: pt
Funcionalidade: Catálogo de produtos
  Como usuário autenticado
  Quero visualizar e ordenar os produtos
  Para encontrar o que procuro

  Contexto:
    Dado que estou autenticado como "standard_user"

  Cenário: CT-G06 - Listagem de produtos após login
    Quando acesso a página de produtos
    Então devo visualizar 6 produtos listados
    E cada produto deve exibir nome, preço e imagem

  Cenário: CT-G07 - Ordenar por preço do menor para o maior
    Quando seleciono a ordenação "Price (low to high)"
    Então os preços devem estar em ordem crescente
    E o primeiro produto deve custar 7.99

  Cenário: CT-G08 - Ordenar por preço do maior para o menor
    Quando seleciono a ordenação "Price (high to low)"
    Então os preços devem estar em ordem decrescente
    E o primeiro produto deve custar 49.99

  Cenário: CT-G09 - Ordenar por nome de A a Z
    Quando seleciono a ordenação "Name (A to Z)"
    Então os nomes devem estar em ordem alfabética crescente
    E o primeiro produto deve ser "Sauce Labs Backpack"

  Cenário: CT-G10 - Ordenar por nome de Z a A
    Quando seleciono a ordenação "Name (Z to A)"
    Então os nomes devem estar em ordem alfabética decrescente
    E o primeiro produto deve ser "Test.allTheThings() T-Shirt (Red)"

  Cenário: CT-G11 - Ver detalhes de um produto
    Quando abro os detalhes do produto "Sauce Labs Backpack"
    Então o nome, a descrição e o preço devem ser exibidos
    E o botão "Add to cart" deve estar disponível
    E o botão "Back to products" deve estar disponível
