saldo = 1000.00  # Saldo inicial

dados = {

'senha': 123,
'conta':0,
'ag':0

}

print('Insira o cartão:')
senha = int(input('Digite sua senha '))

while senha == dados['senha'] and dados['conta']==0 and dados["ag"] == 0:

    while True:
        print("\nEscolha uma opção:")
        print("1. Consultar saldo")
        print("2. Depositar")
        print("3. Sacar")
        print("4. Sair")
        
        opcao = int(input("Digite o número da opção desejada: "))
        
        if opcao == 1:
            print(f"Saldo atual: R$ {saldo:.2f}")
            
        elif opcao == 2:
            deposito = float(input("Informe o valor a ser depositado: R$ "))
            saldo += deposito
            print(f"Depósito de R$ {deposito:.2f} realizado com sucesso.")
            
        elif opcao == 3:
            saque = float(input("Informe o valor a ser sacado: R$ "))
            if saque > saldo:
                print("Saldo insuficiente para realizar o saque.")
            else:
                saldo -= saque
                print(f"Saque de R$ {saque:.2f} realizado com sucesso.")
        
        elif opcao == 4:
            print("Saindo... Até logo!")
            break
        
        else:
            print("Opção inválida. Tente novamente.")

input('Digite enter para sair')
