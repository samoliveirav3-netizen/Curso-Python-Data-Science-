dados  =  {'login':[], 'senha':[]}

login  =  input('login: ')
senha  =  input('Senha: ')

dados['login'].append(login)
dados['senha'].append(senha)

print('dados salvos com sucesso...')

senha_dig = input('Digite a senha para acessar: ')
login_dig = input('Login: ')

if senha_dig in dados['senha'] and login_dig in dados['login']:
    print('Seja bem vindo(a) ao e-commerce!')

    carrinho = []
    meu_total = []
    produtos = ["Camiseta,","Calca,","Tenis"]
    preços = [50,40,30]
    op = input("Deseja Comprar,s ou n?:")
    if op == "n":
        print("Obrigado!Volte Sempre!")   
    else:
        print("Produtos")
        print(produtos)
        escolha = int(input("Camiseta = 0, Calca = 1, Tenis = 2:"))
        carrinho.append(produtos[escolha])
        print(carrinho)
        meu_total.append(preços[escolha])
        soma = sum(meu_total)
        print("R$:",soma)
        op2 = input("Deseja continuar,s ou n?:")
        if op2 == "n":
            pagamento = ["Pix = 0,","Credito = 1,","Debito = 2,"]
            print(pagamento)
            escolha_pag = int(input("Digite o Numero:"))
            print("Voce pagou no",soma,"no", pagamento[escolha_pag]) 
            
        else: 
            print("Produtos")
            print(produtos)
            escolha = int(input("Camiseta = 0, Calca = 1, Tenis = 2:"))
            carrinho.append(produtos[escolha])
            print(carrinho)
            meu_total.append(preços[escolha])
            soma = sum(meu_total)
            print("R$:",soma)
            op3 = input("Deseja continuar,s ou n?:")
            if op3 == "n":
               pagamento = ["Pix = 0,","Credito = 1,","Debito = 2,"]               
               print(pagamento)
               escolha_pag = int(input("Digite o Numero:", ))               
               print("Voce pagou no",soma,"no",pagamento[escolha_pag])
            else: 
               print("Produtos")
               print(produtos)
               escolha = int(input("Camiseta = 0, Calca = 1, Tenis = 2:"))
               carrinho.append(produtos[escolha])
               print(carrinho)
               meu_total.append(preços[escolha])
               soma = sum(meu_total)
               print("R$:",soma)
               pagamento = ["Pix = 0,","Credito = 1,","Debito = 2,"]               
               print(pagamento)
               escolha_pag = int(input("Digite o Numero:"))
               print("Voce pagou no",soma,"no",pagamento[escolha_pag])               
               
         




        
        