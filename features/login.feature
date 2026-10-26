# language: pt
Funcionalidade: Login
  Como usuário do Saucedemo
  Quero autenticar com minhas credenciais
  Para acessar a lista de produtos

  Cenário: CT-G01 - Login com credenciais válidas
    Dado que acesso a página de login do Saucedemo
    Quando preencho o campo Nome de usuário com "standard_user"
    E preencho o campo Senha com "secret_sauce"
    E clico no botão Login
    Então devo ser redirecionado para a página de produtos
    E devo visualizar a lista de produtos disponíveis

  Cenário: CT-G02 - Login com credenciais inválidas
    Dado que acesso a página de login do Saucedemo
    Quando preencho o campo Nome de usuário com "usuario_invalido"
    E preencho o campo Senha com "senha_errada"
    E clico no botão Login
    Então devo permanecer na tela de login
    E devo visualizar a mensagem de erro "Username and password do not match any user in this service"

  Cenário: CT-G03 - Login com senha incorreta
    Dado que acesso a página de login do Saucedemo
    Quando preencho o campo Nome de usuário com "standard_user"
    E preencho o campo Senha com "senha_errada"
    E clico no botão Login
    Então devo permanecer na tela de login
    E devo visualizar a mensagem de erro "Username and password do not match any user in this service"

  Cenário: CT-G04 - Login com campos em branco
    Dado que acesso a página de login do Saucedemo
    Quando deixo o campo Nome de usuário em branco
    E deixo o campo Senha em branco
    E clico no botão Login
    Então devo permanecer na tela de login
    E devo visualizar a mensagem de erro "Username is required"

  Cenário: CT-G05 - Login com senha em branco
    Dado que acesso a página de login do Saucedemo
    Quando preencho o campo Nome de usuário com "standard_user"
    E deixo o campo Senha em branco
    E clico no botão Login
    Então devo permanecer na tela de login
    E devo visualizar a mensagem de erro "Password is required"
