# ============================================================
# PANDEX DEV IND.
# Sistema de Controle de Produção e Qualidade
# Projeto de Algoritmos e Lógica da Programação
# Professor: Grilho
# ============================================================


# -----------------------------
# Configurações do sistema
# -----------------------------

CAPACIDADE_CAIXA = 10

PESO_MINIMO = 95
PESO_MAXIMO = 105

COMPRIMENTO_MINIMO = 10
COMPRIMENTO_MAXIMO = 20

CORES_PERMITIDAS = ["azul", "verde"]


# -----------------------------
# Estruturas de armazenamento
# -----------------------------

pecas = []

caixas_fechadas = []

caixa_atual = []


# -----------------------------
# Função para validar uma peça
# -----------------------------

def avaliar_peca(peso, cor, comprimento):
    motivos = []

    # Verificação do peso
    if peso < PESO_MINIMO or peso > PESO_MAXIMO:
        motivos.append(
            f"Peso fora do padrão ({PESO_MINIMO}g a {PESO_MAXIMO}g)"
        )

    # Verificação da cor
    if cor.lower() not in CORES_PERMITIDAS:
        motivos.append(
            "Cor não permitida (somente azul ou verde)"
        )

    # Verificação do comprimento
    if comprimento < COMPRIMENTO_MINIMO or comprimento > COMPRIMENTO_MAXIMO:
        motivos.append(
            f"Comprimento fora do padrão ({COMPRIMENTO_MINIMO}cm a "
            f"{COMPRIMENTO_MAXIMO}cm)"
        )

    # Se não houver nenhum motivo, a peça está aprovada
    if len(motivos) == 0:
        return True, []

    return False, motivos


# -----------------------------
# Função para cadastrar peça
# -----------------------------

def cadastrar_peca():

    print("\n========== CADASTRO DE PEÇA ==========")

    try:

        identificador = input("Digite o ID da peça: ").strip()

        # Verifica se o ID já existe
        for peca in pecas:
            if peca["id"] == identificador:
                print("Erro: já existe uma peça cadastrada com esse ID.")
                return

        peso = float(input("Digite o peso da peça (g): "))

        cor = input("Digite a cor da peça: ").strip().lower()

        comprimento = float(
            input("Digite o comprimento da peça (cm): ")
        )

        # Avaliação da peça
        aprovada, motivos = avaliar_peca(
            peso,
            cor,
            comprimento
        )

        # Criação do registro
        peca = {
            "id": identificador,
            "peso": peso,
            "cor": cor,
            "comprimento": comprimento,
            "status": "Aprovada" if aprovada else "Reprovada",
            "motivos": motivos
        }

        pecas.append(peca)

        # Se aprovada, adiciona à caixa atual
        if aprovada:

            caixa_atual.append(peca)

            print("\n✓ PEÇA APROVADA!")

            print(
                f"Peças na caixa atual: "
                f"{len(caixa_atual)}/{CAPACIDADE_CAIXA}"
            )

            # Verifica se a caixa atingiu a capacidade
            if len(caixa_atual) == CAPACIDADE_CAIXA:

                caixas_fechadas.append(caixa_atual.copy())

                caixa_atual.clear()

                print("\n📦 CAIXA FECHADA!")
                print("A capacidade máxima de 10 peças foi atingida.")
                print("Uma nova caixa está disponível.")

        else:

            print("\n✗ PEÇA REPROVADA!")

            print("Motivo(s):")

            for motivo in motivos:
                print(f"- {motivo}")

    except ValueError:

        print(
            "\nErro: informe valores numéricos válidos "
            "para peso e comprimento."
        )


# -----------------------------
# Listar peças
# -----------------------------

def listar_pecas():

    print("\n========== LISTA DE PEÇAS ==========")

    if len(pecas) == 0:

        print("Nenhuma peça cadastrada.")

        return

    for peca in pecas:

        print("\n-----------------------------------")

        print(f"ID: {peca['id']}")
        print(f"Peso: {peca['peso']}g")
        print(f"Cor: {peca['cor']}")
        print(f"Comprimento: {peca['comprimento']}cm")
        print(f"Status: {peca['status']}")

        if peca["status"] == "Reprovada":

            print("Motivo(s):")

            for motivo in peca["motivos"]:
                print(f"- {motivo}")


# -----------------------------
# Remover peça
# -----------------------------

def remover_peca():

    print("\n========== REMOVER PEÇA ==========")

    identificador = input(
        "Digite o ID da peça que deseja remover: "
    ).strip()

    encontrada = None

    for peca in pecas:

        if peca["id"] == identificador:

            encontrada = peca
            break

    if encontrada is None:

        print("Peça não encontrada.")

        return

    # Impede a remoção de uma peça que já esteja em caixa fechada
    for caixa in caixas_fechadas:

        for peca_caixa in caixa:

            if peca_caixa["id"] == identificador:

                print(
                    "Não é possível remover esta peça, "
                    "pois ela pertence a uma caixa já fechada."
                )

                return

    # Remove da lista geral
    pecas.remove(encontrada)

    # Caso seja uma peça aprovada, remove também da caixa atual
    if encontrada in caixa_atual:

        caixa_atual.remove(encontrada)

    print("Peça removida com sucesso.")


# -----------------------------
# Listar caixas fechadas
# -----------------------------

def listar_caixas():

    print("\n========== CAIXAS FECHADAS ==========")

    if len(caixas_fechadas) == 0:

        print("Nenhuma caixa foi fechada ainda.")

        return

    for numero, caixa in enumerate(caixas_fechadas, start=1):

        print(f"\n📦 CAIXA {numero}")
        print(f"Quantidade de peças: {len(caixa)}")

        print("Peças:")

        for peca in caixa:

            print(
                f"- ID: {peca['id']} | "
                f"Peso: {peca['peso']}g | "
                f"Cor: {peca['cor']} | "
                f"Comprimento: {peca['comprimento']}cm"
            )


# -----------------------------
# Relatório final
# -----------------------------

def gerar_relatorio():

    print("\n========== RELATÓRIO FINAL ==========")

    total = len(pecas)

    aprovadas = 0
    reprovadas = 0

    motivos_reprovacao = {}

    for peca in pecas:

        if peca["status"] == "Aprovada":

            aprovadas += 1

        else:

            reprovadas += 1

            for motivo in peca["motivos"]:

                if motivo not in motivos_reprovacao:

                    motivos_reprovacao[motivo] = 0

                motivos_reprovacao[motivo] += 1

    # Quantidade de caixas fechadas
    total_caixas_fechadas = len(caixas_fechadas)

    # Caixa em utilização
    if len(caixa_atual) > 0:

        caixas_utilizadas = total_caixas_fechadas + 1

    else:

        caixas_utilizadas = total_caixas_fechadas

    print(f"\nTotal de peças cadastradas: {total}")
    print(f"Total de peças aprovadas: {aprovadas}")
    print(f"Total de peças reprovadas: {reprovadas}")

    print("\nMotivos das reprovações:")

    if len(motivos_reprovacao) == 0:

        print("Nenhuma peça foi reprovada.")

    else:

        for motivo, quantidade in motivos_reprovacao.items():

            print(
                f"- {motivo}: {quantidade} ocorrência(s)"
            )

    print(
        f"\nCaixas fechadas: {total_caixas_fechadas}"
    )

    print(
        f"Caixas utilizadas: {caixas_utilizadas}"
    )

    print(
        f"Peças na caixa atual: {len(caixa_atual)}"
    )


# -----------------------------
# Menu principal
# -----------------------------

def menu():

    while True:

        print("\n")
        print("=" * 55)
        print("       PANDEX DEV IND.")
        print(" SISTEMA DE CONTROLE DE PRODUÇÃO")
        print("=" * 55)

        print("\n1. Cadastrar nova peça")
        print("2. Listar peças aprovadas/reprovadas")
        print("3. Remover peça cadastrada")
        print("4. Listar caixas fechadas")
        print("5. Gerar relatório final")
        print("0. Sair")

        opcao = input(
            "\nDigite uma opção: "
        ).strip()

        if opcao == "1":

            cadastrar_peca()

        elif opcao == "2":

            listar_pecas()

        elif opcao == "3":

            remover_peca()

        elif opcao == "4":

            listar_caixas()

        elif opcao == "5":

            gerar_relatorio()

        elif opcao == "0":

            print("\nSistema encerrado.")
            print("Obrigado por utilizar o sistema PANDEX DEV IND.")

            break

        else:

            print(
                "\nOpção inválida. "
                "Digite uma opção disponível no menu."
            )


# -----------------------------
# Execução do programa
# -----------------------------

if __name__ == "__main__":

    menu()