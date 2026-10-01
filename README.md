# 🏭 PANDEX DEV IND. — Sistema de Controle de Produção e Qualidade

## 📚 Projeto de Algoritmos e Lógica da Programação

**Professor:** Grilho
**Empresa:** PANDEX DEV IND.
**Linguagem:** Python
**Área:** Automação Industrial / Controle de Qualidade

---

## 📋 Sumário

* [1. Sobre o Projeto](#1-sobre-o-projeto)
* [2. Contextualização do Desafio](#2-contextualização-do-desafio)
* [3. Objetivo](#3-objetivo)
* [4. Regras de Qualidade](#4-regras-de-qualidade)
* [5. Estrutura da Lógica](#5-estrutura-da-lógica)
* [6. Funcionalidades](#6-funcionalidades)
* [7. Funcionamento do Sistema](#7-funcionamento-do-sistema)
* [8. Estrutura do Projeto](#8-estrutura-do-projeto)
* [9. Como Executar](#9-como-executar)
* [10. Exemplos de Entrada e Saída](#10-exemplos-de-entrada-e-saída)
* [11. Armazenamento em Caixas](#11-armazenamento-em-caixas)
* [12. Relatório Final](#12-relatório-final)
* [13. Técnicas e Boas Práticas](#13-técnicas-e-boas-práticas)
* [14. Benefícios da Solução](#14-benefícios-da-solução)
* [15. Desafios Encontrados](#15-desafios-encontrados)
* [16. Expansão para um Cenário Real](#16-expansão-para-um-cenário-real)
* [17. Problema Industrial Resolvido](#17-problema-industrial-resolvido)
* [18. Conclusão](#18-conclusão)
* [19. Repositório](#19-repositório)

---

# 1. Sobre o Projeto

O projeto **PANDEX DEV IND. — Sistema de Controle de Produção e Qualidade** foi desenvolvido como atividade da disciplina de **Algoritmos e Lógica da Programação**.

A proposta consiste em desenvolver um protótipo em Python capaz de automatizar parte do processo de inspeção de peças produzidas em uma linha industrial.

O sistema recebe informações sobre cada peça fabricada, realiza automaticamente a avaliação de qualidade e determina se ela deve ser **aprovada ou reprovada**.

As peças aprovadas são organizadas automaticamente em caixas com capacidade máxima de 10 peças.

---

# 2. Contextualização do Desafio

Em ambientes industriais, o controle de qualidade é uma etapa importante para garantir que os produtos fabricados estejam dentro dos padrões estabelecidos pela empresa.

Quando esse processo é realizado exclusivamente de forma manual, podem ocorrer problemas como:

* Falhas de conferência;
* Erros humanos;
* Atrasos na inspeção;
* Dificuldade de controle das peças produzidas;
* Aumento dos custos operacionais;
* Dificuldade na geração de relatórios.

A automação permite transformar regras de qualidade em processos lógicos executados pelo computador.

Neste projeto, o sistema substitui uma conferência manual simples por uma avaliação automática baseada em critérios previamente definidos.

---

# 3. Objetivo

O objetivo principal é desenvolver um sistema em Python capaz de:

1. Receber os dados de cada peça;
2. Avaliar automaticamente os critérios de qualidade;
3. Classificar a peça como aprovada ou reprovada;
4. Informar os motivos da reprovação;
5. Armazenar peças aprovadas em caixas;
6. Fechar automaticamente as caixas quando atingirem 10 peças;
7. Permitir consultar e remover peças cadastradas;
8. Exibir as caixas fechadas;
9. Gerar um relatório consolidado da produção.

---

# 4. Regras de Qualidade

Para uma peça ser considerada aprovada, ela precisa atender simultaneamente aos três critérios definidos pela PANDEX DEV IND.

| Critério       | Regra             |
| -------------- | ----------------- |
| ⚖️ Peso        | Entre 95g e 105g  |
| 🎨 Cor         | Azul ou verde     |
| 📏 Comprimento | Entre 10cm e 20cm |

A peça somente será aprovada quando **todos os critérios forem atendidos**.

### ✅ Exemplo de peça aprovada

```text
ID: P001
Peso: 100g
Cor: azul
Comprimento: 15cm
```

Resultado:

```text
APROVADA
```

### ❌ Exemplo de peça reprovada

```text
ID: P002
Peso: 110g
Cor: azul
Comprimento: 15cm
```

Resultado:

```text
REPROVADA
Motivo:
Peso fora do padrão.
```

---

# 5. Estrutura da Lógica

A solução foi estruturada utilizando conceitos fundamentais de **Algoritmos e Lógica da Programação**.

## 5.1 Variáveis

São utilizadas variáveis para armazenar informações como:

* ID da peça;
* Peso;
* Cor;
* Comprimento;
* Status;
* Motivos da reprovação;
* Quantidade de peças;
* Quantidade de caixas.

---

## 5.2 Condições

As estruturas condicionais `if`, `elif` e `else` são utilizadas para tomar decisões.

Por exemplo:

```python
if peso < 95 or peso > 105:
    motivos.append("Peso fora do padrão")
```

Essa condição verifica se o peso está fora do intervalo permitido.

---

## 5.3 Repetição

O sistema utiliza estruturas `for` e `while`.

O `while` mantém o menu funcionando até que o usuário escolha a opção de saída:

```python
while True:
    ...
```

Já o `for` é utilizado para percorrer peças, caixas e motivos de reprovação.

---

## 5.4 Funções

O programa foi dividido em funções para facilitar a organização, manutenção e reutilização do código.

Principais funções:

```text
avaliar_peca()
cadastrar_peca()
listar_pecas()
remover_peca()
listar_caixas()
gerar_relatorio()
menu()
```

Essa divisão evita concentrar toda a lógica em um único bloco de código.

---

# 6. Funcionalidades

O sistema possui um menu interativo com as seguintes opções:

```text
1. Cadastrar nova peça
2. Listar peças aprovadas/reprovadas
3. Remover peça cadastrada
4. Listar caixas fechadas
5. Gerar relatório final
0. Sair
```

## 6.1 Cadastrar nova peça

Permite informar:

* ID;
* Peso;
* Cor;
* Comprimento.

Após o cadastro, o sistema verifica automaticamente os critérios de qualidade.

---

## 6.2 Listar peças

Exibe todas as peças cadastradas e informa:

* ID;
* Peso;
* Cor;
* Comprimento;
* Status;
* Motivo da reprovação, quando aplicável.

---

## 6.3 Remover peça

Permite remover uma peça utilizando seu ID.

Peças pertencentes a caixas já fechadas não podem ser removidas, preservando a integridade do processo de embalagem.

---

## 6.4 Listar caixas fechadas

Exibe todas as caixas que atingiram a capacidade máxima de 10 peças.

---

## 6.5 Gerar relatório

O relatório apresenta:

* Total de peças cadastradas;
* Total de peças aprovadas;
* Total de peças reprovadas;
* Motivos das reprovações;
* Quantidade de caixas fechadas;
* Quantidade de caixas utilizadas;
* Quantidade de peças na caixa atual.

---

# 7. Funcionamento do Sistema

O fluxo básico do programa é:

```text
                         ┌───────────┐
                         │   INÍCIO  │
                         └─────┬─────┘
                               │
                               ▼
                       ┌───────────────┐
                       │ Exibir Menu   │
                       └───────┬───────┘
                               │
                               ▼
                       ┌───────────────┐
                       │ Cadastrar     │
                       │ nova peça     │
                       └───────┬───────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │ Receber dados da peça│
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │ Avaliar critérios    │
                    │ Peso / Cor / Tamanho │
                    └──────────┬───────────┘
                               │
                         ┌─────┴─────┐
                         │ Aprovada? │
                         └─────┬─────┘
                               │
                   ┌───────────┴───────────┐
                   │                       │
                  SIM                     NÃO
                   │                       │
                   ▼                       ▼
             ┌───────────┐          ┌────────────┐
             │ Adicionar │          │ Registrar  │
             │ à caixa   │          │ reprovação │
             └─────┬─────┘          └──────┬─────┘
                   │                       │
                   ▼                       │
             ┌───────────────┐             │
             │ Caixa possui  │             │
             │ 10 peças?     │             │
             └───────┬───────┘             │
                     │                     │
                ┌────┴────┐                │
               SIM       NÃO               │
                │          │               │
                ▼          │               │
          ┌───────────┐    │               │
          │ Fechar    │    │               │
          │ caixa     │    │               │
          └─────┬─────┘    │               │
                │          │               │
                └────┬─────┴───────────────┘
                     │
                     ▼
               ┌─────────────┐
               │ Voltar Menu │
               └──────┬──────┘
                      │
                      ▼
                   ┌──────┐
                   │ FIM  │
                   └──────┘
```

---

# 8. Estrutura do Projeto

O projeto possui a seguinte estrutura:

```text
pandex-controle-producao/
│
├── README.md
├── sistema.py
└── .gitignore
```

### `README.md`

Documento contendo a explicação teórica e prática do projeto.

### `sistema.py`

Arquivo contendo o código-fonte completo do sistema.

### `.gitignore`

Arquivo utilizado para evitar o envio ao GitHub de arquivos desnecessários.

---

# 9. Como Executar

## Pré-requisitos

É necessário possuir o **Python 3.x** instalado no computador.

Para verificar a instalação:

```bash
python --version
```

No Windows também pode ser utilizado:

```bash
py --version
```

---

## Passo 1 — Clonar o projeto

No terminal:

```bash
git https://github.com/lcsmaster13/pandex-controle-producao
```

Depois, acesse a pasta:

```bash
cd pandex-controle-producao
```

---

## Passo 2 — Executar o programa

Execute:

```bash
python sistema.py
```

Em alguns ambientes Windows:

```bash
py sistema.py
```

---

## Passo 3 — Utilizar o menu

Após executar o programa, o menu será apresentado:

```text
=======================================================
       PANDEX DEV IND.
 SISTEMA DE CONTROLE DE PRODUÇÃO
=======================================================

1. Cadastrar nova peça
2. Listar peças aprovadas/reprovadas
3. Remover peça cadastrada
4. Listar caixas fechadas
5. Gerar relatório final
0. Sair
```

---

# 10. Exemplos de Entrada e Saída

## Exemplo 1 — Peça aprovada

### Entrada

```text
ID: P001
Peso: 100
Cor: azul
Comprimento: 15
```

### Saída

```text
✓ PEÇA APROVADA!

Peças na caixa atual: 1/10
```

---

## Exemplo 2 — Peça reprovada por peso

### Entrada

```text
ID: P002
Peso: 110
Cor: azul
Comprimento: 15
```

### Saída

```text
✗ PEÇA REPROVADA!

Motivo(s):

- Peso fora do padrão (95g a 105g)
```

---

## Exemplo 3 — Peça reprovada por cor

### Entrada

```text
ID: P003
Peso: 100
Cor: vermelho
Comprimento: 15
```

### Saída

```text
✗ PEÇA REPROVADA!

Motivo(s):

- Cor não permitida (somente azul ou verde)
```

---

## Exemplo 4 — Peça reprovada por múltiplos critérios

### Entrada

```text
ID: P004
Peso: 120
Cor: vermelho
Comprimento: 25
```

### Saída

```text
✗ PEÇA REPROVADA!

Motivo(s):

- Peso fora do padrão (95g a 105g)
- Cor não permitida (somente azul ou verde)
- Comprimento fora do padrão (10cm a 20cm)
```

---

# 11. Armazenamento em Caixas

As peças aprovadas são armazenadas automaticamente na caixa atual.

Cada caixa possui capacidade máxima de:

```text
10 peças
```

Quando a décima peça aprovada é inserida, o sistema fecha automaticamente a caixa:

```text
📦 CAIXA FECHADA!

A capacidade máxima de 10 peças foi atingida.

Uma nova caixa está disponível.
```

O sistema então inicia automaticamente uma nova caixa para as próximas peças aprovadas.

### Regra importante

Somente peças **aprovadas** podem ser armazenadas nas caixas.

Peças reprovadas permanecem registradas no sistema, mas não são adicionadas às caixas.

---

# 12. Relatório Final

O relatório consolida os dados do processo de produção.

### Exemplo

```text
========== RELATÓRIO FINAL ==========

Total de peças cadastradas: 25
Total de peças aprovadas: 20
Total de peças reprovadas: 5

Motivos das reprovações:

- Peso fora do padrão (95g a 105g): 2 ocorrência(s)
- Cor não permitida (somente azul ou verde): 2 ocorrência(s)
- Comprimento fora do padrão (10cm a 20cm): 1 ocorrência(s)

Caixas fechadas: 2
Caixas utilizadas: 3
Peças na caixa atual: 0
```

Esse relatório permite uma visão consolidada da produção realizada durante a execução do programa.

---

# 13. Técnicas e Boas Práticas

Durante o desenvolvimento foram aplicados conceitos importantes de programação.

## Modularização

O programa foi dividido em funções específicas para cada responsabilidade.

## Validação de dados

O programa utiliza `try/except` para evitar que entradas inválidas causem o encerramento inesperado do sistema.

## Estruturas condicionais

Foram utilizadas estruturas `if`, `elif` e `else` para implementar as regras de qualidade.

## Estruturas de repetição

Foram utilizados `for` e `while` para percorrer dados e manter o menu funcionando.

## Listas

As listas são utilizadas para armazenar:

* Peças;
* Peças da caixa atual;
* Caixas fechadas;
* Motivos de reprovação.

## Dicionários

Cada peça é armazenada como um dicionário contendo seus respectivos dados.

Exemplo:

```python
{
    "id": "P001",
    "peso": 100,
    "cor": "azul",
    "comprimento": 15,
    "status": "Aprovada",
    "motivos": []
}
```

## Constantes

Os critérios de qualidade foram definidos no início do programa:

```python
PESO_MINIMO = 95
PESO_MAXIMO = 105

COMPRIMENTO_MINIMO = 10
COMPRIMENTO_MAXIMO = 20

CAPACIDADE_CAIXA = 10
```

Essa abordagem facilita futuras alterações nas regras do sistema.

---

# 14. Benefícios da Solução

O protótipo apresenta alguns benefícios para o processo industrial:

* Redução da conferência manual;
* Padronização dos critérios de qualidade;
* Identificação automática de peças reprovadas;
* Registro dos motivos de reprovação;
* Organização das peças aprovadas;
* Controle automático da capacidade das caixas;
* Geração de informações consolidadas;
* Redução da possibilidade de erros de conferência.

Além disso, a estrutura modular facilita futuras melhorias no sistema.

---

# 15. Desafios Encontrados

Durante o desenvolvimento, alguns pontos exigiram atenção.

Um dos principais desafios foi estruturar corretamente as regras de aprovação para que todos os critérios fossem considerados simultaneamente.

Outro ponto importante foi controlar a capacidade das caixas. O sistema precisava adicionar somente peças aprovadas e fechar automaticamente uma caixa ao atingir 10 peças.

Também foi necessário pensar no tratamento das peças reprovadas, permitindo registrar mais de um motivo quando a peça não atendesse a vários critérios simultaneamente.

Por fim, foi necessário organizar o código em funções para evitar que todas as operações ficassem concentradas no menu principal.

---

# 16. Expansão para um Cenário Real

Apesar de ser um protótipo desenvolvido em Python, a solução poderia ser expandida para utilização em um ambiente industrial real.

## 🔌 Sensores

Sensores poderiam coletar automaticamente:

* Peso;
* Comprimento;
* Cor;
* Dimensões;
* Temperatura;
* Outras características físicas.

Em vez de o operador digitar os valores, os dados poderiam ser enviados diretamente para o sistema.

---

## 🤖 Inteligência Artificial

Uma futura versão poderia utilizar Inteligência Artificial e visão computacional para identificar defeitos nas peças.

Uma câmera industrial poderia capturar imagens e um modelo de IA poderia detectar:

* Rachaduras;
* Arranhões;
* Alterações de cor;
* Deformações;
* Problemas de acabamento.

---

## 🏭 Integração Industrial

O sistema também poderia ser integrado a equipamentos e plataformas industriais utilizando tecnologias como:

* APIs;
* Banco de dados;
* Sistemas ERP;
* Sistemas MES;
* CLPs;
* IoT industrial.

Dessa forma, os dados poderiam ser registrados automaticamente e acompanhados em tempo real.

---

## 📊 Dashboard

Outra evolução seria a criação de um painel de controle mostrando indicadores como:

```text
Produção total
Peças aprovadas
Peças reprovadas
Taxa de aprovação
Taxa de reprovação
Caixas produzidas
Principais motivos de reprovação
```

---

# 17. Problema Industrial Resolvido

O problema abordado neste projeto é a necessidade de automatizar uma etapa do processo de inspeção de qualidade da PANDEX DEV IND.

O sistema reduz a dependência de uma conferência exclusivamente manual ao transformar critérios de qualidade em regras computacionais.

A partir dos dados fornecidos, o programa consegue determinar automaticamente a situação da peça e organizar as peças aprovadas para armazenamento.

Assim, o protótipo demonstra como conceitos básicos de algoritmos podem ser utilizados para solucionar problemas encontrados em processos industriais.

---

# 18. Conclusão

O desenvolvimento do sistema **PANDEX DEV IND. — Sistema de Controle de Produção e Qualidade** permitiu aplicar na prática conceitos fundamentais de **Algoritmos e Lógica da Programação**.

Foram utilizados conceitos como:

* Variáveis;
* Operadores;
* Estruturas condicionais;
* Estruturas de repetição;
* Funções;
* Listas;
* Dicionários;
* Validação de dados;
* Modularização.

O projeto demonstra que uma tarefa inicialmente realizada de forma manual pode ser transformada em um processo automatizado utilizando regras lógicas.

Embora o sistema desenvolvido seja um protótipo acadêmico, sua estrutura permite imaginar uma evolução para um ambiente industrial integrado, utilizando sensores, banco de dados, Inteligência Artificial, Internet das Coisas e sistemas de gestão industrial.

Dessa forma, o projeto demonstra a importância da programação como ferramenta para automatizar processos, reduzir erros e apoiar a gestão da produção e do controle de qualidade em ambientes industriais.

---

# 19. Repositório

O código-fonte completo do projeto está disponível no GitHub:

🔗 **Repositório:** https://github.com/lcsmaster13/pandex-controle-producao
---

## 👨‍💻 Autor

**Lucas Eduardo Cunha de Oliveira**

Projeto acadêmico desenvolvido para a disciplina de **Algoritmos e Lógica da Programação**.

**Professor:** Grillo

---

## 📌 Tecnologias utilizadas

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge\&logo=python)

![GitHub](https://img.shields.io/badge/GitHub-Repositório-black?style=for-the-badge\&logo=github)

![Status](https://img.shields.io/badge/Status-Concluído-success?style=for-the-badge)

---

> **PANDEX DEV IND. — Tecnologia, automação e qualidade para a indústria.** 🏭🤖
