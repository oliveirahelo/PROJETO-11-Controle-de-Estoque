# PROJETO 11 — Controle de Estoque
# Autor: Professor Ricardo Rodrigues Lima
# Linguagem: Python 3

def linha():
    print("-" * 60)

def mostrar_menu():
    print("""
📦 MENU DE OPÇÕES:
[1] Cadastrar produto
[2] Registrar entrada no estoque
[3] Registrar saída no estoque
[4] Mostrar relatório completo
[5] Sair
""")

def cadastrar_produto(estoque):
    nome = input("Digite o nome do produto: ").strip()
    if nome in estoque:
        print("⚠️ Produto já cadastrado!")
        return
    try:
        quantidade = int(input("Digite a quantidade inicial: "))
        preco = float(input("Digite o preço unitário (R$): "))
        estoque[nome] = {"quantidade": quantidade, "preco": preco}
        print(f"✅ Produto '{nome}' cadastrado com sucesso!")
    except ValueError:
        print("❌ Valores inválidos. Tente novamente.")

def entrada_estoque(estoque):
    nome = input("Digite o nome do produto para adicionar: ").strip()
    if nome not in estoque:
        print("❌ Produto não encontrado!")
        return
    try:
        qtd = int(input("Quantidade a adicionar: "))
        estoque[nome]["quantidade"] += qtd
        print(f"✅ Entrada registrada! Estoque atual: {estoque[nome]['quantidade']}")
    except ValueError:
        print("⚠️ Quantidade inválida.")

def saida_estoque(estoque):
    nome = input("Digite o nome do produto para retirar: ").strip()
    if nome not in estoque:
        print("❌ Produto não encontrado!")
        return
    try:
        qtd = int(input("Quantidade a retirar: "))
        if qtd > estoque[nome]["quantidade"]:
            print("⚠️ Quantidade insuficiente no estoque!")
        else:
            estoque[nome]["quantidade"] -= qtd
            print(f"✅ Saída registrada! Estoque atual: {estoque[nome]['quantidade']}")
    except ValueError:
        print("⚠️ Quantidade inválida.")

def relatorio(estoque):
    if not estoque:
        print("📭 Nenhum produto cadastrado.")
        return

    linha()
    print(f"{'PRODUTO':<20}{'QTD':<10}{'PREÇO (R$)':<15}{'TOTAL (R$)':<15}")
    linha()

    total_geral = 0
    for nome, dados in estoque.items():
        total = dados["quantidade"] * dados["preco"]
        total_geral += total
        print(f"{nome:<20}{dados['quantidade']:<10}{dados['preco']:<15.2f}{total:<15.2f}")

    linha()
    print(f"💰 Valor total do estoque: R${total_geral:.2f}")
    linha()

def main():
    estoque = {}
    print("=" * 60)
    print("🏪 SISTEMA DE CONTROLE DE ESTOQUE")
    print("=" * 60)

    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_produto(estoque)
        elif opcao == "2":
            entrada_estoque(estoque)
        elif opcao == "3":
            saida_estoque(estoque)
        elif opcao == "4":
            relatorio(estoque)
        elif opcao == "5":
            print("✅ Encerrando o sistema. Até logo!")
            break
        else:
            print("❌ Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()