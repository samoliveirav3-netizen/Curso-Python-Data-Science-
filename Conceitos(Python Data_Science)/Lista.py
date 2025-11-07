lista = [10,20,30]
lists = [40,60,70]
print(lista)
lista.insert(0, 1)               #Colocar algo na lista!
print(lista)
lista.extend([90,78,120])
print([lista] + [lists])
#--------------------------------------------------------]
lista.remove(1)
print(lista)
del lista[0]                 #Para retirar algo
lista.pop(2)
print(lista)
#---------------------------------------------------------]
print(max(lista))
print(min(lista))
print(lista.count(20))
print(lista.copy())       #Outros comandos
print(lista.clear)
print(sum(lista))

i = list(range(1, 2026))
print(i)

