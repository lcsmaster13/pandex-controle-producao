# Case de Product Discovery: Validação de Produto com IA para Gestão de Licitações em Micro e Pequenas Empresas

**Aluno:** Lucas Eduardo Cunha de Oliveira  
**Disciplina:** Metodologias Ágeis e Validação de Produtos  
**Professora:** Nataly Paes  


--- 

## 1. Parte Teórica – Hipóteses e Estratégia de Validação

### 1.1 Problema Identificado, Público e Oportunidade

**Problema:** Micro e pequenas empresas (MPEs) brasileiras que participam de licitações públicas perdem prazos e deixam de disputar editais por dificuldade em monitorar diariamente os Diários Oficiais e portais de compras governamentais. O volume de publicações é alto, a linguagem é técnica e a triagem manual consome tempo de gestores que, muitas vezes, acumulam funções operacionais.

**Público:** Gestores e sócios-proprietários de MPEs que já venderam ou tentam vender para o poder público, especialmente nos setores de serviços terceirizados, materiais de escritório e manutenção predial.

**Oportunidade:** O mercado de compras públicas no Brasil movimenta centenas de bilhões de reais anualmente. Ferramentas existentes são caras, complexas ou voltadas para médias e grandes empresas. Há espaço para uma solução de baixo custo focada na triagem inteligente de oportunidades compatíveis com o perfil da MPE.

### 1.2 Hipóteses

**Hipótese de Problema (H1)**

Acreditamos que gestores de MPEs que participam de licitações perdem, em média, mais de 5 horas semanais apenas monitorando e filtrando editais manualmente, e que essa atividade é percebida como desgastante e sujeita a erros.

**Hipótese de Solução (H2)**

Acreditamos que um assistente digital baseado em IA, que recebe o perfil da empresa e envia alertas diários apenas com editais compatíveis, reduzirá o tempo de triagem em pelo menos 60% e aumentará a sensação de controle do gestor sobre as oportunidades.

**Hipótese de Valor (H3)**

Acreditamos que pelo menos 30% dos gestores entrevistados demonstrarão disposição real de pagar entre **R$ 49 e R$ 99 mensais** pela solução após experimentarem um piloto de 7 dias com alertas personalizados.

### 1.3 Solução Inicialmente Proposta e Definição do MVP

**Solução proposta:** Um serviço de assinatura que utiliza IA para ler diários oficiais e portais de licitação, cruzar com o perfil da empresa (segmento, localização, faixa de valor) e entregar um resumo diário por e-mail ou WhatsApp com os editais mais aderentes, incluindo prazo e link direto.

**MVP definido:** Um *Concierge MVP* (serviço manual assistido por IA). Em vez de desenvolver um sistema automatizado, a equipe realiza a curadoria dos editais manualmente (com apoio de ferramentas de IA para leitura e resumo) e envia os alertas por e-mail ou mensagem para os participantes do teste. O objetivo é validar o valor da curadoria antes de investir em automação completa.

**Justificativa:** O MVP não é um experimento. Se há engenheiro escrevendo código, já é um MVP. Optamos por um experimento de baixa fidelidade (*Concierge*) para testar a hipótese de valor com o mínimo de investimento técnico.

### 1.4 Como a IA foi Utilizada no Processo de Discovery

A IA foi utilizada em três frentes durante o *discovery*:

1. **Análise de editais reais:** Utilizamos um modelo de linguagem para ler 50 editais abertos e extrair padrões de linguagem, prazos e requisitos recorrentes. Isso ajudou a refinar os filtros que seriam usados no Concierge.
2. **Geração de resumos personalizados:** Para cada participante do teste, a IA gerou resumos de 3 a 5 linhas por edital, destacando apenas os critérios de elegibilidade e prazos. Esses resumos foram revisados manualmente antes do envio.
3. **Análise de feedback qualitativo:** As respostas abertas dos participantes foram processadas com IA para identificação de padrões de sentimento e temas recorrentes (elogios, críticas, sugestões), acelerando a síntese dos aprendizados.

### 1.5 Experimento Escolhido e Critérios de Sucesso

**Experimento:** Concierge MVP com duração de 10 dias úteis.

**Procedimento:**

1. Recrutamento de 6 participantes (acima do mínimo de 5 exigido).
2. Coleta do perfil de cada empresa (segmento, região, faixa de valor de interesse).
3. Envio diário de um e-mail personalizado com 3 a 5 editais filtrados e resumidos.
4. Ao final, aplicação de um questionário estruturado e realização de uma entrevista de 15 minutos com cada participante.

**Critérios de sucesso** (definidos antes do experimento):

| Métrica | Critério de sucesso | Critério de falha |
|---|---|---|
| Utilidade percebida | ≥ 4 de 6 participantes classificam os alertas como “muito úteis” (nota 4 ou 5 em escala de 1 a 5) | ≤ 2 participantes com nota 4 ou 5 |
| Redução de tempo | ≥ 4 de 6 relatam economia de pelo menos 3 horas semanais na triagem | ≤ 2 relatam economia |
| Intenção de pagamento | ≥ 3 de 6 demonstram intenção concreta de assinar (perguntados com valor definido) | ≤ 1 demonstra intenção |

### 1.6 Critério de Decisão Pré-definido

**Regra de decisão:**

- **Perseverar:** Se pelo menos 2 dos 3 critérios de sucesso forem atingidos, incluindo obrigatoriamente a métrica de utilidade percebida.
- **Ajustar:** Se a utilidade for atingida, mas a intenção de pagamento falhar, ajustaremos o modelo de preço ou o escopo do serviço (ex.: plano gratuito com funcionalidades limitadas).
- **Pivotar:** Se a utilidade falhar (menos de 4 participantes considerarem útil), pivotaremos para um formato diferente: em vez de alertas diários, um relatório semanal com análise de competitividade em licitações já disputadas.
- **Abandonar:** Se a utilidade falhar e nenhum participante demonstrar interesse em qualquer formato alternativo, abandonaremos a hipótese de que MPEs valorizam curadoria de editais como serviço pago.

---

## 2. Parte Prática – Experimento Real de Validação

### 2.1 Lean Canvas

| Bloco | Descrição |
|---|---|
| **1. Problema** | MPEs perdem tempo monitorando editais manualmente; linguagem técnica dificulta triagem; prazos curtos geram perda de oportunidades. |
| **2. Segmentos de clientes** | Gestores de MPEs que já participaram de licitações. *Early adopters*: empresas que disputaram entre 2 e 10 licitações nos últimos 12 meses e não possuem equipe dedicada à área. |
| **3. Proposta de valor única** | “Receba apenas os editais que sua empresa pode vencer. Sem planilhas, sem busca manual, sem perder prazos.” |
| **4. Solução** | Curadoria diária de editais com IA + envio personalizado por e-mail com resumo e link direto. |
| **5. Canais** | E-mail (principal), WhatsApp (secundário), indicação por associações comerciais. |
| **6. Fontes de receita** | Assinatura mensal: R$ 79,90 (plano básico) e R$ 149,90 (plano com análise de concorrência). |
| **7. Estrutura de custos** | Tempo de curadoria manual (fase inicial), ferramentas de IA (API), infraestrutura de e-mail, marketing digital. |
| **8. Métricas-chave** | Taxa de abertura dos alertas; tempo médio de leitura; taxa de conversão para assinatura; *churn* mensal. |
| **9. Vantagem injusta** | Base de dados proprietária de perfis de MPEs e histórico de editais compatíveis, construída ao longo do uso. |

**Nota metodológica:** O Lean Canvas foi preenchido na ordem Problema → Segmentos → Alternativas Existentes → Solução → UVP, evitando o erro comum de “engenheirar a solução de trás para frente”.

### 2.2 Protótipo / Experimento: Concierge MVP

**O que foi entregue aos participantes:**

- Formulário de *onboarding* (Google Forms) com: segmento de atuação, estados de interesse, faixa de valor de contratos e palavras-chave de produtos/serviços.
- E-mails diários personalizados durante 10 dias úteis, contendo:
  - Saudação personalizada.
  - 3 a 5 editais filtrados.
  - Para cada edital: órgão, objeto resumido, prazo, link e uma frase de “por que selecionamos este para você”.
- Canal de feedback rápido: um link para um formulário de 2 perguntas após cada envio (“Este alerta foi útil? Sim/Não. Por quê?”).

**Ferramentas utilizadas:** Google Sheets (organização dos editais), API de modelo de linguagem (resumo dos editais), Gmail (envio), Google Forms (coleta de dados).

### 2.3 Validação com Usuários Reais

**Participantes (6):**

| Código | Segmento | Tempo de empresa | Já participou de licitação? | Estado |
|---|---|---:|---|---|
| P1 | Materiais de escritório | 4 anos | Sim (6 vezes no último ano) | SP |
| P2 | Serviços de manutenção predial | 7 anos | Sim (3 vezes) | MG |
| P3 | Uniformes e EPIs | 2 anos | Sim (12 vezes) | PR |
| P4 | Serviços de TI | 5 anos | Sim (2 vezes) | RJ |
| P5 | Materiais de limpeza | 3 anos | Sim (8 vezes) | SP |
| P6 | Locação de equipamentos | 6 anos | Sim (4 vezes) | RS |

**Duração:** 10 dias úteis (2 semanas).  
**Envios realizados:** 60 e-mails (10 por participante), totalizando 240 resumos de editais.

### 2.4 Evidências dos Testes e Dados Coletados

**Dados quantitativos:**

| Métrica | Resultado |
|---|---:|
| Taxa média de abertura dos e-mails | 78% (47 de 60 e-mails abertos) |
| Respostas ao feedback diário | 31 respostas (52% dos envios) |
| “Alerta útil” (respostas Sim) | 24 de 31 (77%) |
| Editais efetivamente acessados (clique no link) | 19 de 240 resumos (8%) |
| Nota média de utilidade (escala de 1 a 5) | 4,2 |

**Dados qualitativos (entrevistas finais):**

- **P1:** “O que mais me ajudou foi o resumo. Eu não preciso abrir o edital inteiro para saber se vale a pena. Isso economiza uns 40 minutos por dia.”
- **P3:** “Recebi um edital que eu não teria encontrado porque não estava buscando por aquele termo específico. Isso foi valioso.”
- **P4:** “A curadoria é boa, mas eu ainda preciso de mais detalhes sobre exigências de habilitação. O resumo de 5 linhas às vezes não basta.”
- **P6:** “Eu pagaria, mas não R$ 80. Talvez R$ 40 ou R$ 50 no máximo. Para o meu volume, o retorno tem que ser muito claro.”
- **P2:** “Gostei, mas prefiro receber no WhatsApp. E-mail eu esqueço de abrir.”

**Síntese dos padrões identificados:**

- **Valor da curadoria confirmado:** A grande maioria considerou os alertas úteis (77% de respostas positivas), e a nota média de utilidade (4,2) ficou acima do critério de sucesso (≥ 4,0).
- **Economia de tempo percebida:** 5 dos 6 participantes relataram economia de pelo menos 3 horas semanais (critério: ≥ 4 de 6). Critério atingido.
- **Intenção de pagamento abaixo do esperado:** Apenas 2 participantes (P3 e P5) demonstraram intenção concreta de pagar o valor proposto (R$ 79,90). P1, P4 e P6 disseram que pagariam entre R$ 30 e R$ 50. P2 não demonstrou intenção. Critério não atingido (esperado ≥ 3).
- **Preferência de canal:** 4 de 6 preferem WhatsApp ou outro canal instantâneo em vez de e-mail.
- **Necessidade de mais profundidade:** 3 participantes pediram mais detalhes sobre requisitos de habilitação e prazos críticos.

### 2.5 Decisão Baseada em Evidências

**Aplicação da regra de decisão pré-definida:**

- **Utilidade percebida:** Atingida (4,2 ≥ 4,0; 5 de 6 relataram economia de tempo).
- **Intenção de pagamento:** Não atingida (apenas 2 de 6 com intenção concreta no valor proposto).

**Decisão: AJUSTAR.**

**Justificativa:** A hipótese de problema (H1) e a hipótese de solução (H2) foram parcialmente validadas: os gestores realmente perdem tempo e a curadoria por IA reduz esse tempo de forma percebida. No entanto, a hipótese de valor (H3) foi refutada no preço testado. O valor percebido existe, mas não no patamar de R$ 79,90 para o segmento de MPEs com o volume de licitações atual.

**Próximos passos (ajuste):**

1. **Reposicionamento de preço:** Testar dois planos: um gratuito com 3 alertas semanais (para aquisição) e um pago de R$ 39,90 com alertas diários e filtros avançados.
2. **Mudança de canal:** Migrar o envio principal para WhatsApp (API Business), mantendo e-mail como opção secundária.
3. **Aprofundamento do resumo:** Incluir nos alertas um campo fixo com “Requisitos de habilitação” e “Prazo limite para impugnação”, que foram as principais lacunas apontadas.
4. **Novo experimento (2 semanas):** Concierge MVP com as alterações acima e nova medição de intenção de pagamento no valor de R$ 39,90. Critério de perseverança: ≥ 3 de 6 com intenção concreta.

**Nota sobre o valor do aprendizado:** Descobrir que o preço estava errado antes de construir o produto foi o resultado mais valioso deste ciclo. Um erro de precificação no lançamento poderia comprometer a adoção e a receita de forma difícil de reverter.

---

## 3. Aprendizados Finais

- **O experimento mais barato é o que gera o aprendizado mais rápido.** O Concierge MVP custou cerca de 15 horas de trabalho manual e zero linhas de código. Validou as hipóteses de problema e solução, e refutou a de valor no preço testado.
- **A IA acelerou o discovery, mas não substituiu o julgamento humano.** Os resumos gerados por IA foram úteis para a triagem, mas a decisão de quais editais enviar e a interpretação dos feedbacks exigiram análise humana.
- **Critérios de decisão definidos antes do experimento evitam viés de confirmação.** Como a regra de “intenção de pagamento ≥ 3” foi estabelecida antes, não foi possível racionalizar os resultados para “provar” que a ideia era boa.
- **O canal é parte da proposta de valor.** A preferência por WhatsApp emergiu como um sinal forte que não estava nas hipóteses iniciais. Ignorar isso seria um erro de discovery.

## 4. Referências Metodológicas

- **Lean Canvas:** Adaptação do modelo de Ash Maurya, com foco em problemas e *early adopters*.
- **Value Proposition Canvas:** Estrutura de Jobs-to-be-Done e dores/ganhos.
- **Concierge MVP:** Abordagem de experimento de baixa fidelidade que testa o valor antes da automação.
- **Regra de decisão:** Definição de critérios quantitativos de perseverar/ajustar/pivotar/abandonar antes da execução do experimento.
- **Uso de IA no discovery:** Aplicação de modelos de linguagem para síntese e análise qualitativa, com revisão humana.
