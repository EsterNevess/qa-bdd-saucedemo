# BDD com pytest-bdd — Saucedemo

[![Testes BDD](https://github.com/EsterNevess/qa-bdd-saucedemo/actions/workflows/ci.yml/badge.svg)](https://github.com/EsterNevess/qa-bdd-saucedemo/actions/workflows/ci.yml)
[![Relatório Allure](https://img.shields.io/badge/Relat%C3%B3rio-Allure-FF5722?logo=qase&logoColor=white)](https://esternevess.github.io/qa-bdd-saucedemo/)

📊 **[Relatório Allure da última execução](https://esternevess.github.io/qa-bdd-saucedemo/)** — publicado automaticamente a cada push, com histórico das últimas 20 execuções.

Automação dos **13 cenários Gherkin** que eu havia escrito e executado manualmente em
[qa-saucedemo-teste-manual](https://github.com/EsterNevess/qa-saucedemo-teste-manual).
Lá eles eram documentação; aqui eles rodam.

A ideia do projeto é essa: **o mesmo texto que o time de negócio lê é o que a automação executa.**
Nenhum cenário foi reescrito para caber na ferramenta — os arquivos `.feature` mantêm a redação
original em português, com `Dado`, `Quando` e `Então`.

| | |
|---|---|
| Cenários | 13, todos passando |
| Tempo de execução | ~17 s |
| Stack | Python · pytest-bdd · Playwright · pytest-html · GitHub Actions |
| Alvo | https://www.saucedemo.com |

## O que está coberto

| Arquivo | Cenários | O que verifica |
|---|---|---|
| `features/login.feature` | CT-G01 a CT-G05 | credenciais válidas, inválidas, senha incorreta, campos em branco |
| `features/produtos.feature` | CT-G06 a CT-G11 | listagem, as quatro ordenações e a página de detalhe |
| `features/carrinho.feature` | CT-G12 e CT-G13 | adicionar e remover produto, com o contador do carrinho |

As ordenações não são verificadas só pelo primeiro item: a asserção compara a lista inteira contra
`sorted()`, porque um filtro pode acertar o topo e errar o meio.

## Estrutura

```
features/          cenários em Gherkin, em português
pages/             Page Object Model (login e produtos)
tests/             steps do pytest-bdd + fixtures
.github/workflows/ execução automática a cada push
```

A separação é proposital: o `.feature` descreve **o que** se espera, o step traduz para ação, e o
Page Object concentra **como** a página é acessada. Quando um seletor muda, muda em um lugar só.

## Evidência de falha

O `conftest.py` tem um hook que, quando um cenário falha, captura três coisas e as anexa ao
relatório Allure: **print da tela inteira**, **URL no momento da falha** e **HTML da página**.

O print também vai para `evidencias/` em disco, para quem está rodando localmente. A duplicação é
proposital: quem depura na própria máquina quer o arquivo à mão; quem só vai abrir o relatório
publicado precisa da evidência dentro dele. Print que ninguém encontra não é evidência.

## Relatório Allure

O [relatório](https://esternevess.github.io/qa-bdd-saucedemo/) é gerado e publicado no GitHub Pages
a cada push, e guarda o **histórico das últimas 20 execuções** — o que permite ver tendência, e não
só a foto do momento. Teste que falha de vez em quando aparece no gráfico de histórico; numa
execução isolada, não.

O CI roda os testes com `continue-on-error` e só depois devolve o resultado real ao job. Parece
contraintuitivo, mas é necessário: sem isso, o pipeline morre na falha e o relatório **não** é
publicado — justamente quando ele seria mais útil. O passo final garante que o selo do README
continue refletindo a verdade.

## Como rodar

```bash
python -m venv venv
venv\Scripts\activate          # Linux/macOS: source venv/bin/activate
pip install -r requirements.txt
python -m playwright install chromium
pytest
```

O relatório é gerado em `relatorio.html`.

Para ver o navegador durante a execução:

```bash
pytest --headed --slowmo 500
```

## Decisões que vale explicar

**Por que pytest-bdd e não Behave ou Robot Framework.** O pytest-bdd roda sobre o pytest, então eu
aproveito fixtures, plugins e o ecossistema que já uso no meu
[projeto de automação de API e Web](https://github.com/EsterNevess/qa-automation-serverest).

**Por que os cenários continuam em português.** BDD existe para aproximar quem escreve o requisito
de quem testa. Traduzir o cenário para inglês para caber na ferramenta derrota o propósito —
o pytest-bdd aceita `# language: pt` e resolve.

**Por que não há espera fixa.** Nenhum `sleep` no código: o Playwright espera o elemento ficar
acionável antes de agir. Espera fixa é a origem mais comum de teste instável.
