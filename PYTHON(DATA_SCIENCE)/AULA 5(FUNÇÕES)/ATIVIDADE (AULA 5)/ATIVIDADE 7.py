def calcular():
    print('____Calculadora____')
    
    
    

def soma(a,b):
    soma = a + b
    print('A soma deu:',soma)
    
    
    
    
def subtração(a,b):
    subtração = a - b
    print('A subtração deu:',subtração)
    
    
    
    
def multiplicação(a,b):
    multiplicação = a * b
    print('A multiplicação deu:',multiplicação)
    
    
    
    
def divisão(a,b):
    if a == '0' or b == '0':
        print('Não pode dividir por zero')
    else:
        divisão = a / b
        print('A divisão deu:',divisão)



    

calcular()
while True:
  a = int(input('Digite um numero:'))
  b = int(input('Digite um numero:'))

  operacao = input('Qual operação voce quer escolher,+,-,* ou /:')
  if operacao == '+':
    soma(a,b)
  elif operacao == '-':
    subtração(a,b)
  elif operacao == '*':
    multiplicação(a,b)
  elif operacao == '/':
    divisão(a,b)
  else:
    print('Errado')