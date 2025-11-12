#Funcoes:
#print()/input()/len()/max()/min()/sum()
#4 lugares:
#Da linguagem/De Pacotes internos e externos/Criando funcoes
#[-------------------------------------------------------------]#
#def nome(nome1):
   #if nome1 == "Sam":
      #print("Bom Dia,",nome1)
   #else: 
      #print("Errado") 


#nome1 = input("Nome:")      
    

#nome(nome1)
#[--------------------------------------------------------------]#
#def display():
    #nome = input('Digite o nome:')
    #sobrenome = input('Digite o sobrenome')
    #print(nome, sobrenome)


#def imc():
    #altura =  float(input('Altura: '))
    #peso = float(input('Peso: '))
    #imc  =  peso / altura**2
    #print(imc)    


#display()
#imc()
#-----------------------------------------------------------------
#def verificarO_indice(num,lista):
    #indice  =  lista.index(num)
    #print(indice)



#lista  =  [102,35,5,6]
#n  = int(input('numero: '))


#verificarO_indice(n, lista)
#------------------------------------------------------------------
# SISTEMA DE CALCULO HORAS 
# 1 -  calculo da hora normal
def cal_val_hr(carga, salario):
    return salario / carga


# 2 -  hora exta 
def hora_extra(valor_hora):
    return valor_hora * 1.5


# 3 -  quantas horas extrar realizadas
def quantidade_extra(quantidade, valor_hr_extra):
    return quantidade * valor_hr_extra


# 4 - total salário
def sal(total_extra, salario):
    return total_extra +  salario


def sistema():
    salario  =  float(input('Salario: '))
    quantidade_ex =  float(input('Hora extra: '))
    carga  = float(input('Carga: '))


    valor_hora  =  cal_val_hr(carga, salario)
    print('VALOR HORA R$', round(valor_hora, 2))
    print('----------------------')


    extra  =  hora_extra(valor_hora)
    print('VALOR DA HORA EXTRA R$:', round(extra,2))


    print('----------------------')
    quantidade_ = quantidade_extra(quantidade_ex,extra )
    print('TOTAL HORA EXTRA R$', round(quantidade_,2))
    print('----------------------')
    
    salario_t = sal(quantidade_,salario)
    print('Salario total: R$', round(salario_t,2))


    print('----------------------')
    
sistema()    




 
