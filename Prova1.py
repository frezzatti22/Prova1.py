 #funcoes_estoque.py

def analisar_estoque(estoque):
    if not estoque:
        print("Estoque vazio.")
        return

    limite = 5
    print(f"--- Análise (Limite de Baixo Estoque: {limite}) ---")

    maior_valor = 0
    menor_valor = float('inf')
    produto_maior = ""
    produto_menor = ""
    total_geral = 0

    print("Produtos com estoque baixo:")
    for p in estoque:
        if p['qtd'] <= limite:
            print(f"- {p['nome']} (apenas {p['qtd']} restantes)")

        valor_item = p['qtd'] * p['preco']
        total_geral += valor_item

        if valor_item > maior_valor:
            maior_valor = valor_item
            produto_maior = p['nome']

        if valor_item < menor_valor:
            menor_valor = valor_item
            produto_menor = p['nome']

    print(f"Produto de MAIOR valor total: {produto_maior} (R$ {maior_valor:.2f})")
    print(f"Produto de MENOR valor total: {produto_menor} (R$ {menor_valor:.2f})")
    print(f"Valor GERAL do estoque: R$ {total_geral:.2f}")

def relatorio_final(estoque, operacoes):
    print("=== RELATÓRIO FINAL ===")
    if not operacoes:
        print("Nenhuma operação registrada ainda.")
        
    for op in operacoes:
        print(f"- {op}")

    print(f"Total de produtos diferentes: {len(estoque)}")

    total = sum(p['qtd'] * p['preco'] for p in estoque)
    print(f"Valor total do estoque: R$ {total:.2f}")