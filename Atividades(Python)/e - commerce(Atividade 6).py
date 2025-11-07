# Crie um sistema para controle de estoque de uma loja, onde:
# O sistema pode adicionar novos produtos com nome, quantidade e preço.
# O sistema pode vender um produto, reduzindo sua quantidade no estoque.
# O sistema pode listar todos os produtos em estoque.
# O sistema deve garantir que a quantidade de um produto não seja negativa.



# Informe o nome do produto: Arroz
# Informe a quantidade: 100
# Informe o preço unitário: 5.0

# Escolha uma opção:
# 1. Adicionar produto
# 2. Vender produto
# 3. Ver estoque
# 4. Sair
# 2
# Informe o nome do produto a ser vendido: Arroz
# Informe a quantidade a ser vendida: 10
# Venda realizada! Quantidade de Arroz em estoque: 90


# Estoque:
# - Arroz: 90 unidades, R$ 5.00 cada
carrinho = []
while True:
    print("\nEscolha uma opção:")
    print("1. Adicionar produto")
    print("2. Remover produto")
    print("3. Ver carrinho")
    print("4. Calcular total")
    print("5. Sair")
    
    opcao = int(input("Digite o número da opção desejada: "))
    
    if opcao == 1:
        nome = input("Informe o nome do produto: ")
        preco = float(input("Informe o preço do produto: R$ "))
        carrinho.append((nome, preco))
        print(f"Produto {nome} adicionado ao carrinho.")
        
    elif opcao == 2:
        nome_remover = input("Informe o nome do produto a ser removido: ")
        for i, (produto, preco) in enumerate(carrinho):
            if produto.lower() == nome_remover.lower():
                carrinho.pop(i)
                print(f"Produto {nome_remover} removido do carrinho.")
                break
        else:
            print("Produto não encontrado no carrinho.")
    
    elif opcao == 3:
        if not carrinho:
            print("O carrinho está vazio.")
        else:
            print("Carrinho de compras:")
            for produto, preco in carrinho:
                print(f"- {produto}: R$ {preco:.2f}")
    
    elif opcao == 4:
        total = sum(preco for _, preco in carrinho)
        print(f"Total da compra: R$ {total:.2f}")
    
    elif opcao == 5:
        print("Saindo... Até logo!")
        break
    
    else:
        print("Opção inválida. Tente novamente.")

input("Digite enter para sair")            