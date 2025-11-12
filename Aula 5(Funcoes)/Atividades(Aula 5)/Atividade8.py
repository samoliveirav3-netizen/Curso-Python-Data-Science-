#1 - Com funções crie um sistema de médias notas escolares*** 

#2 - Com funções crie um sistema de para calcular o IMC***

#3 - Com funções crie um jogo da adivinhação***
#--------------------------------------------------------------------
import random
def medias(nome):
    notas = [10,5,6] 
    nomes = [nome]
    nome = notas[0]
    soma_das_listas = [sum(notas)]
    media_da_nome = soma_das_listas[0] / 3
    print("Nome:",nomes)
    print("Notas",notas)
    print("Nota Total:",soma_das_listas)
    print("A Media da/o ",nome,":",media_da_nome)








def imc(nome):
    print(nome)
    peso = float(input("Peso:"))
    altura = float(input("Altura:"))
    imc = peso / altura**2
    print(imc)








def adivinhacao():
    numero_aleatorio =  random.randint(1,10)
    meu_chute = int(input('chute: '))
    if meu_chute == numero_aleatorio:
        print('Acertou em cheio!O número é: ', numero_aleatorio)
    else:
        print('Errou feio!O número é: ', numero_aleatorio)




def play():
    nome = input("Nome:")
    while True:
        op = input(""""""
               
    "1.Media"
    "2.Imc"
    "3.Jogo da Adivinhacao"          
       ":"        "")
        if op == "1":
            medias(nome)
        elif op == "2":
            imc(nome)
        elif op == "3":
            adivinhacao()
        else:
            print("Errado")        
        

play()


