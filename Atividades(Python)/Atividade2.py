print("----Sistema Escolar----")
print("Fazendo a Media:")
notas = [[10,10,10],[5,2,3],[5,9,8],[10,0,6]] 
nomes = ['Ana','Fernanda', 'Caio', 'Fernando']
Ana = notas[0]
Fernanda = notas[1]
Caio = notas[2]
Fernando = notas[3]
soma_das_listas = [sum(sublista) for sublista in notas]
media_da_Ana = soma_das_listas[0] / 3
media_da_Fernanda = soma_das_listas[1] / 3
media_da_Caio = soma_das_listas[2] / 3
media_da_Fernando = soma_das_listas[3] / 3
media_geral = media_da_Ana + media_da_Fernanda + media_da_Caio + media_da_Fernando  / 12
print(soma_das_listas)
print("A Media da Ana:")
print(media_da_Ana)
print("A Media da Fernanda:")
print(media_da_Fernanda)
print("A Media da Caio:")
print(media_da_Caio)
print("A Media da Fernando:")
print(media_da_Fernando)
print("A maior media foi:")
print(max(media_da_Ana,media_da_Fernanda,media_da_Caio,media_da_Fernando))
print("A Media Geral foi:")
print(media_geral)