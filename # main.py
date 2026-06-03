# main.py

# Importa as funções do arquivo que criamos acima
from Prova1 import analisar_estoque, relatorio_final

def main():
    estoque = []
    operacoes = []

    while True:
        print("\n=== MENU ===")
        print("1. Cadastrar Produto")
        print("2. Movimentar Estoque")
        print("3. Análise")
        print("4. Relatório")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            nome = input("Nome: ")
            categoria = input("Categoria: ")
            try:
                qtd = int(input("Quantidade: "))
                preco = float(input("Preço: "))
                pos = int(input(f"Posição para inserir (0 a {len(estoque)}): "))

                if 0 <= pos <= len(estoque):
                    estoque.insert(pos, {"nome": nome, "categoria": categoria, "qtd": qtd, "preco": preco})
                    operacoes.append(f"Cadastrou '{nome}' na posição {pos}")
                    print("Produto cadastrado com sucesso!")
                else:
                    print("Erro: Posição inválida!")
            except ValueError:
                print("Erro: Digite apenas números válidos para quantidade, preço e posição.")

        elif opcao == '2':
            busca = input("\nNome do produto ou Posição: ")
            encontrou = False

            for i, p in enumerate(estoque):
                if p['nome'].lower() == busca.lower() or str(i) == busca:
                    encontrou = True
                    mov = input("Entrada (E) ou Saída (S)? ").upper()
                    try:
                        qtd_mov = int(input("Quantidade: "))
                        if mov == 'E':
                            p['qtd'] += qtd_mov
                            operacoes.append(f"Entrada de {qtd_mov} unidades de '{p['nome']}'")
                            print("Entrada realizada com sucesso!")
                        elif mov == 'S':
                            if p['qtd'] >= qtd_mov:
                                p['qtd'] -= qtd_mov
                                operacoes.append(f"Saída de {qtd_mov} unidades de '{p['nome']}'")
                                print("Saída realizada com sucesso!")
                            else:
                                print(f"Erro: Estoque insuficiente! Existem {p['qtd']} unidades.")
                        else:
                            print("Opção inválida.")
                    except ValueError:
                        print("Erro: Digite um número válido.")
                    break

            if not encontrou:
                print("Produto não encontrado!")

        elif opcao == '3':
            analisar_estoque(estoque)

        elif opcao == '4':
            relatorio_final(estoque, operacoes)
            
        elif opcao == '5':
            print("Saindo do programa...")
            break

        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()