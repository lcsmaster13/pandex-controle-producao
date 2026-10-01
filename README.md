🏭 PANDEX DEV IND. — Sistema de Controle de Produção e Qualidade
📚 Projeto de Algoritmos e Lógica da Programação

Professor: Grilho
Empresa: PANDEX DEV IND.
Linguagem: Python
Área: Automação Industrial / Controle de Qualidade

📋 Sumário
1. Sobre o Projeto
2. Contextualização do Desafio
3. Objetivo
4. Regras de Qualidade
5. Estrutura da Lógica
6. Funcionalidades
7. Funcionamento do Sistema
8. Estrutura do Projeto
9. Como Executar
10. Exemplos de Entrada e Saída
11. Armazenamento em Caixas
12. Relatório Final
13. Técnicas e Boas Práticas
14. Benefícios da Solução
15. Desafios Encontrados
16. Expansão para um Cenário Real
17. Problema Industrial Resolvido
18. Conclusão
19. Repositório
1. Sobre o Projeto

O projeto PANDEX DEV IND. — Sistema de Controle de Produção e Qualidade foi desenvolvido como atividade da disciplina de Algoritmos e Lógica da Programação.

A proposta consiste em desenvolver um protótipo em Python capaz de automatizar parte do processo de inspeção de peças produzidas em uma linha industrial.

O sistema recebe informações sobre cada peça fabricada, realiza automaticamente a avaliação de qualidade e determina se ela deve ser aprovada ou reprovada.

As peças aprovadas são organizadas automaticamente em caixas com capacidade máxima de 10 peças.

2. Contextualização do Desafio

Em ambientes industriais, o controle de qualidade é uma etapa importante para garantir que os produtos fabricados estejam dentro dos padrões estabelecidos pela empresa.

Quando esse processo é realizado exclusivamente de forma manual, podem ocorrer problemas como:

Falhas de conferência;
Erros humanos;
Atrasos na inspeção;
Dificuldade de controle das peças produzidas;
Aumento dos custos operacionais;
Dificuldade na geração de relatórios.

A automação permite transformar regras de qualidade em processos lógicos executados pelo computador.

Neste projeto, o sistema substitui uma conferência manual simples por uma avaliação automática baseada em critérios previamente definidos.

3. Objetivo

O objetivo principal é desenvolver um sistema em Python capaz de:

Receber os dados de cada peça;
Avaliar automaticamente os critérios de qualidade;
Classificar a peça como aprovada ou reprovada;
Informar os motivos da reprovação;
Armazenar peças aprovadas em caixas;
Fechar automaticamente as caixas quando atingirem 10 peças;
Permitir consultar e remover peças cadastradas;
Exibir as caixas fechadas;
Gerar um relatório consolidado da produção.
4. Regras de Qualidade

Para uma peça ser considerada aprovada, ela precisa atender simultaneamente aos três critérios definidos pela PANDEX DEV IND.

Critério	Regra
Peso	Entre 95g e 105g
Cor	Azul ou verde
Comprimento	Entre 10cm e 20cm

A peça somente será aprovada quando todos os critérios forem atendidos.

Exemplo de peça aprovada
ID: P001
Peso: 100g
Cor: azul
Comprimento: 15cm

Resultado:

APROVADA
Exemplo de peça reprovada
ID: P002
Peso: 110g
Cor: azul
Comprimento: 15cm

Resultado:

REPROVADA
Motivo:
Peso fora do padrão.
5. Estrutura da Lógica

A solução foi estruturada utilizando conceitos fundamentais de algoritmos e lógica da programação.

5.1 Variáveis

São utilizadas variáveis para armazenar informações como:

ID da peça;
Peso;
Cor;
Comprimento;
Status;
Motivos da reprovação;
Quantidade de peças;
Quantidade de caixas.
5.2 Condições

As estruturas condicionais if, elif e else são utilizadas para tomar decisões.

Por exemplo:

if peso < 95 or peso > 105:
    motivos.append("Peso fora do padrão")

Essa condição verifica se o peso está fora do intervalo permitido.

5.3 Repetição

O sistema utiliza estruturas for e while.

O while mantém o menu funcionando até que o usuário escolha a opção de saída.

while True:
    ...

Já o for é utilizado para percorrer peças, caixas e motivos de reprovação.

5.4 Funções

O programa foi dividido em funções para facilitar a organização e manutenção do código.

Principais funções:

avaliar_peca()
cadastrar_peca()
listar_pecas()
remover_peca()
listar_caixas()
gerar_relatorio()
menu()

Essa divisão evita concentrar toda a lógica em um único bloco de código.

6. Funcionalidades

O sistema possui um menu interativo com as seguintes opções:

1. Cadastrar nova peça
2. Listar peças aprovadas/reprovadas
3. Remover peça cadastrada
4. Listar caixas fechadas
5. Gerar relatório final
0. Sair
6.1 Cadastrar nova peça

Permite informar:

ID;
Peso;
Cor;
Comprimento.

Após o cadastro, o sistema verifica automaticamente os critérios de qualidade.

6.2 Listar peças

Exibe todas as peças cadastradas e informa:

ID;
Peso;
Cor;
Comprimento;
Status;
Motivo da reprovação, quando aplicável.
6.3 Remover peça

Permite remover uma peça utilizando seu ID.

Peças pertencentes a caixas já fechadas não podem ser removidas, preservando a integridade do processo de embalagem.

6.4 Listar caixas fechadas

Exibe todas as caixas que atingiram a capacidade máxima de 10 peças.

6.5 Gerar relatório

O relatório apresenta:

Total de peças cadastradas;
Total de peças aprovadas;
Total de peças reprovadas;
Motivos das reprovações;
Quantidade de caixas fechadas;
Quantidade de caixas utilizadas;
Quantidade de peças na caixa atual.
7. Funcionamento do Sistema

O fluxo básico do programa é:

Início
  ↓
Exibir menu
  ↓
Cadastrar peça
  ↓
Receber dados
  ↓
Validar peso, cor e comprimento
  ↓
 ┌─────────────────┐
 │ Todos aprovados?│
 └────────┬────────┘
          │
     ┌────┴────┐
    SIM       NÃO
     │          │
     ▼          ▼
  Aprovar     Reprovar
     │          │
     ▼          ▼
Adicionar     Registrar
à caixa       motivo
     │
     ▼
Caixa possui 10 peças?
     │
   ┌─┴─┐
  SIM NÃO
   │   │
   ▼   ▼
Fechar Continuar
caixa  caixa
   │
   └──────► Menu
8. Estrutura do Projeto

O projeto possui a seguinte estrutura:

pandex-controle-producao/
│
├── README.md
├── sistema.py
└── .gitignore
README.md

Documento contendo a explicação teórica e prática do projeto.

sistema.py

Arquivo contendo o código-fonte completo do sistema.

.gitignore

Arquivo utilizado para evitar o envio ao GitHub de arquivos desnecessários.

9. Como Executar
Pré-requisitos

É necessário possuir o Python instalado no computador.

A versão recomendada é:

Python 3.x
Passo 1 — Clonar o projeto

No terminal:

git clone URL_DO_REPOSITORIO

Depois:

cd pandex-controle-producao
Passo 2 — Executar o programa

Execute:

python sistema.py

Em alguns ambientes Windows, pode ser necessário utilizar:

python3 sistema.py

ou:

py sistema.py
Passo 3 — Utilizar o menu

Após executar o programa, o menu será apresentado:

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
10. Exemplos de Entrada e Saída
Exemplo 1 — Peça aprovada

Entrada:

ID: P001
Peso: 100
Cor: azul
Comprimento: 15

Saída:

✓ PEÇA APROVADA!

Peças na caixa atual: 1/10
Exemplo 2 — Peça reprovada por peso

Entrada:

ID: P002
Peso: 110
Cor: azul
Comprimento: 15

Saída:

✗ PEÇA REPROVADA!

Motivo(s):

- Peso fora do padrão (95g a 105g)
Exemplo 3 — Peça reprovada por cor

Entrada:

ID: P003
Peso: 100
Cor: vermelho
Comprimento: 15

Saída:

✗ PEÇA REPROVADA!

Motivo(s):

- Cor não permitida (somente azul ou verde)
Exemplo 4 — Peça reprovada por múltiplos critérios

Entrada:

ID: P004
Peso: 120
Cor: vermelho
Comprimento: 25

Saída:

✗ PEÇA REPROVADA!

Motivo(s):

- Peso fora do padrão (95g a 105g)
- Cor não permitida (somente azul ou verde)
- Comprimento fora do padrão (10cm a 20cm)
11. Armazenamento em Caixas

As peças aprovadas são armazenadas automaticamente na caixa atual.

Cada caixa possui capacidade máxima de:

10 peças

Quando a décima peça aprovada é inserida:

📦 CAIXA FECHADA!
A capacidade máxima de 10 peças foi atingida.
Uma nova caixa está disponível.

O sistema então inicia automaticamente uma nova caixa.

12. Relatório Final

O relatório consolida os dados do processo de produção.

Exemplo:

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

Esse relatório permite uma visão consolidada da produção realizada durante a execução do programa.

13. Técnicas e Boas Práticas

Durante o desenvolvimento foram aplicados conceitos importantes de programação.

Modularização

O programa foi dividido em funções específicas para cada responsabilidade.

Validação de dados

O programa utiliza try/except para evitar que entradas inválidas causem o encerramento inesperado do sistema.

Estruturas condicionais

Foram utilizadas estruturas if, elif e else para implementar as regras de qualidade.

Estruturas de repetição

Foram utilizados for e while para percorrer dados e manter o menu funcionando.

Listas

As listas são utilizadas para armazenar:

Peças;
Peças da caixa atual;
Caixas fechadas;
Motivos de reprovação.
Dicionários

Cada peça é armazenada como um dicionário contendo seus respectivos dados.

Exemplo:

{
    "id": "P001",
    "peso": 100,
    "cor": "azul",
    "comprimento": 15,
    "status": "Aprovada",
    "motivos": []
}
Constantes

Os critérios de qualidade foram definidos no início do programa:

PESO_MINIMO = 95
PESO_MAXIMO = 105

COMPRIMENTO_MINIMO = 10
COMPRIMENTO_MAXIMO = 20

CAPACIDADE_CAIXA = 10

Essa abordagem facilita futuras alterações nas regras do sistema.

14. Benefícios da Solução

O protótipo apresenta alguns benefícios para o processo industrial:

Redução da conferência manual;
Padronização dos critérios de qualidade;
Identificação automática de peças reprovadas;
Registro dos motivos de reprovação;
Organização das peças aprovadas;
Controle automático da capacidade das caixas;
Geração de informações consolidadas;
Redução da possibilidade de erros de conferência.

Além disso, a estrutura modular facilita futuras melhorias no sistema.

15. Desafios Encontrados

Durante o desenvolvimento, alguns pontos exigiram atenção.

Um dos principais desafios foi estruturar corretamente as regras de aprovação para que todos os critérios fossem considerados simultaneamente.

Outro ponto importante foi controlar a capacidade das caixas. O sistema precisava adicionar somente peças aprovadas e fechar automaticamente uma caixa ao atingir 10 peças.

Também foi necessário pensar no tratamento das peças reprovadas, permitindo registrar mais de um motivo quando a peça não atendesse a vários critérios simultaneamente.

Por fim, foi necessário organizar o código em funções para evitar que todas as operações ficassem concentradas no menu principal.

16. Expansão para um Cenário Real

Apesar de ser um protótipo desenvolvido em Python, a solução poderia ser expandida para utilização em um ambiente industrial real.

Sensores

Sensores poderiam coletar automaticamente:

Peso;
Comprimento;
Cor;
Dimensões;
Temperatura;
Outras características físicas.

Em vez de o operador digitar os valores, os dados poderiam ser enviados diretamente para o sistema.

Inteligência Artificial

Uma futura versão poderia utilizar Inteligência Artificial e visão computacional para identificar defeitos nas peças.

Uma câmera industrial poderia capturar imagens e um modelo de IA poderia detectar:

Rachaduras;
Arranhões;
Alterações de cor;
Deformações;
Problemas de acabamento.
Integração industrial

O sistema também poderia ser integrado a equipamentos e plataformas industriais utilizando tecnologias como:

APIs;
Banco de dados;
Sistemas ERP;
Sistemas MES;
CLPs;
IoT industrial.

Dessa forma, os dados poderiam ser registrados automaticamente e acompanhados em tempo real.

Dashboard

Outra evolução seria a criação de um painel de controle mostrando indicadores como:

Produção total
Peças aprovadas
Peças reprovadas
Taxa de aprovação
Taxa de reprovação
Caixas produzidas
Principais motivos de reprovação
17. Problema Industrial Resolvido

O problema abordado neste projeto é a necessidade de automatizar uma etapa do processo de inspeção de qualidade da PANDEX DEV IND.

O sistema reduz a dependência de uma conferência exclusivamente manual ao transformar critérios de qualidade em regras computacionais.

A partir dos dados fornecidos, o programa consegue determinar automaticamente a situação da peça e organizar as peças aprovadas para armazenamento.

Assim, o protótipo demonstra como conceitos básicos de algoritmos podem ser utilizados para solucionar problemas encontrados em processos industriais.

18. Conclusão

O desenvolvimento do sistema PANDEX DEV IND. permitiu aplicar na prática conceitos fundamentais de Algoritmos e Lógica da Programação.

Foram utilizados conceitos como variáveis, operadores, estruturas condicionais, estruturas de repetição, funções, listas e dicionários.

O projeto demonstra que uma tarefa inicialmente realizada de forma manual pode ser transformada em um processo automatizado utilizando regras lógicas.

Embora o sistema desenvolvido seja um protótipo acadêmico, sua estrutura permite imaginar uma evolução para um ambiente industrial integrado, utilizando sensores, banco de dados, Inteligência Artificial, Internet das Coisas e sistemas de gestão industrial.

Dessa forma, o projeto demonstra a importância da programação como ferramenta para automatizar processos, reduzir erros e apoiar a tomada de decisões em ambientes industriais.

19. Repositório

O código-fonte completo do projeto está disponível no GitHub:

🔗 Repositório: COLOCAR_LINK_DO_GITHUB_AQUI