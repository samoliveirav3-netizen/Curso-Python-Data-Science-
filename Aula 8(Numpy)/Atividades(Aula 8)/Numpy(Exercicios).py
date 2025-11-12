# # ATIVIDADE 1:

# # Crie um array NumPy [1, 2, 3, 4, 5] e:

# # Multiplique todos os elementos por 10.

# # Calcule a média dos valores.

# # Substitua os números pares por -1.
#Atividade 1:
# import numpy as np
# ar = np.array([1, 2, 3, 4, 5])
# print("A array Numpy:")
# print(ar)
# a = ar * 10
# print("Multiplique todos os elementos por 10:")
# print(a)
# print("Media:")
# m = np.mean(ar)
# print(m)
# print("Substitua os números pares por -1:")
# x = -1
# r = ar [ar % 2 == 0 ] = x
# print(ar)

#--------------------------------------------------------------
# ATIVIDADE 2:

# Crie um array 2D de tamanho (5, 5) com valores aleatórios entre 0 e 100.

# Calcule a média de cada linha.

# Encontre o valor máximo e mínimo de toda a matriz.
# import numpy as np
# matrix_1 = np.array([1,2,3,4,5])
# matrix_2 = np.array([6,7,8,9,10])
# matrix_3 = np.array([11,12,13,14,15])
# matrix_4 = np.array([16,17,18,19,20])
# matrix_5 = np.array([21,22,23,24,25])
# print("Media(Matriz):")
# print("Linha 1",np.mean(matrix_1))
# print("Linha 2",np.mean(matrix_2))
# print("Linha 3",np.mean(matrix_3))
# print("Linha 4",np.mean(matrix_4))
# print("Linha 5",np.mean(matrix_5))
# print("valor Máximo:")
# print("Linha 1:",np.max(matrix_1))
# print("Linha 2",np.max(matrix_2))
# print("Linha 3",np.max(matrix_3))
# print("Linha 4",np.max(matrix_4))
# print("Linha 5",np.max(matrix_5))
# print("Valor Mínimo:")
# print("Linha 1:",np.min(matrix_1))
# print("Linha 2",np.min(matrix_2))
# print("Linha 3",np.min(matrix_3))
# print("Linha 4",np.min(matrix_4))
# print("Linha 5",np.min(matrix_5))

#------------------------------------------------------------------
# 3 - EXPLOQUE A DOCUMENTAÇÃO 


# https://numpy.org/doc/stable/
# Filtre apenas as vendas maiores que 100.

# Calcule quantas vendas ficaram abaixo da média.

# Crie um novo array com os valores (divida cada valor pelo máximo).
# import numpy as np
# vendas = np.array([120,90,150,80,200,110,50,300])
# print("Vendas Maiores que 100:")
# filtro = vendas > 100
# x = vendas[filtro]
# print(x)
# print("Media:")
# media = np.mean(vendas)
# print(media)
# print("Vendas ficaram abaixo da média:")
# filtro_2 = vendas < media
# x_2 = vendas[filtro_2]
# print(x_2)
# print("Maximo:")
# maximo = np.max(vendas)
# print(maximo)
# print("Divida cada valor pelo máximo:")
# filtro_3 = vendas / maximo
# print(filtro_3)
