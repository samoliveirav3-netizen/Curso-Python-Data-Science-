# lista = [1, 2, 3, 4, 5]
# array = np.array(lista)
# print(array)


# Array de zeros:

# zeros = np.zeros(5)
# print(zeros)
# Array de uns:


# ones = np.ones((2, 3))  # Array 2x3
# print(ones)


# Array com valores uniformemente espaçados:

# espacado = np.arange(0, 10, 2)  # Início, fim, passo
# print(espacado)


# Array com valores linearmente espaçados:

# linear = np.linspace(0, 1, 5)  # Início, fim, número de pontos
# print(linear)

# Operações com Arrays
# Operações element-wise:


# a = np.array([1, 2, 3])
# b = np.array([4, 5, 6])
# print(a + b)  # Soma
# print(a - b)  # Subtração
# print(a * b)  # Multiplicação
# print(a / b)  # Divisão


# Funções universais:

# a = np.array([1, 2, 3])
# print(np.sqrt(a))  # Raiz quadrada
# print(np.exp(a))   # Exponencial
# print(np.sin(a))   # Seno


# Estatísticas e Agregações


# Média, variância e desvio padrão:


# dados = np.array([1, 2, 3, 4, 5])
# print(np.mean(dados))      # Média
# print(np.var(dados))       # Variância
# print(np.std(dados))       # Desvio padrão


# Soma e produto:

# dados = np.array([1, 2, 3, 4, 5])
# print(np.sum(dados))       # Soma
# print(np.prod(dados))      # Produto



# Máximo e mínimo:
# dados = np.array([1, 2, 3, 4, 5])
# print(np.max(dados))       # Valor máximo
# print(np.min(dados))    

#    # Valor mínimo
# Manipulação de Arrays

# Redimensionamento:


# dados = np.arange(6)
# dados_reshape = dados.reshape((2, 3))
# print(dados_reshape)



# Indexação e fatiamento:
# dados = np.array([1, 2, 3, 4, 5])
# print(dados[1:4])  # Elementos de 1 a 3
# print(dados[:3])   # Primeiros 3 elementos
# print(dados[::2])  # Elementos com passo 2


# Filtro Booleano:

# dados = np.array([1, 2, 3, 4, 5])
# filtro = dados > 3
# print(dados[filtro])  # Elementos maiores que 3


# Concatenar arrays:

# a = np.array([1, 2, 3])
# b = np.array([4, 5, 6])
# c = np.concatenate((a, b))
# print(c)


# Funções Matemáticas


# Funções de arredondamento:

# dados = np.array([1.2, 2.5, 3.8])
# print(np.round(dados))    # Arredondar ao inteiro mais próximo
# print(np.floor(dados))    # Arredondar para baixo
# print(np.ceil(dados))     # Arredondar para cima



# Trigonometria:

# angulos = np.array([0, np.pi/2, np.pi])
# print(np.sin(angulos))    # Seno
# print(np.cos(angulos))    # Cosseno
# print(np.tan(angulos))    # Tangente



# Operações com matrizes:

# matriz = np.array([[1, 2], [3, 4]])
# print(np.transpose(matriz))   # Transposição
# print(np.linalg.inv(matriz))  # Inversa




# aleatorios =  np.random.randint(0,11)
# aleatorios

# t =  np.random.default_rng()
# teste = t.random((10,5))
# teste



# E em Arrays 3D?
# Para um array (3, 2, 4) (3 blocos, 2 linhas, 4 colunas):

# axis=0 → opera entre blocos.

# axis=1 → opera entre linhas dentro de cada bloco.

# axis=2 → opera entre colunas dentro de cada bloco.


# ------

# # principais funções


# # np.array()
# # Cria arrays (vetores ou matrizes).


# a = np.array([1, 2, 3])
# b = np.array([[1, 2], [3, 4]])




# #  np.arange()
# # Gera uma sequência de números com intervalo definido.


# np.arange(0, 10, 2)  # [0, 2, 4, 6, 8]




# #  np.linspace()
# # Gera uma sequência de números igualmente espaçados.


# np.linspace(0, 1, 5)  # [0. , 0.25, 0.5 , 0.75, 1. ]




# #   np.zeros() e np.ones()
# # Cria arrays preenchidos com zeros ou uns.


# np.zeros((2, 3))  # matriz 2x3 de zeros
# np.ones((3, 2))   # matriz 3x2 de uns




# #  np.reshape()
# # Muda a forma (dimensão) de um array.


# a = np.arange(6)
# a.reshape((2, 3))  # transforma em matriz 2x3




# #  Operações matemáticas
# # Você pode fazer operações diretamente com arrays:


# a = np.array([1, 2, 3])
# b = np.array([4, 5, 6])

# a + b  # [5, 7, 9]
# a * b  # [4, 10, 18]




# #  np.mean(), np.std(), np.sum()
# # Funções estatísticas:


# a = np.array([1, 2, 3, 4])

# np.mean(a)  # média
# np.std(a)   # desvio padrão
# np.sum(a)   # soma




# #  np.dot() e np.matmul()
# # Multiplicação de matrizes:


# a = np.array([[1, 2], [3, 4]])
# b = np.array([[5, 6], [7, 8]])

# np.dot(a, b)
# np.matmul(a, b)




# #   np.random.rand() e np.random.randint()
# # Geração de números aleatórios:


# np.random.rand(2, 3)       # matriz 2x3 com números aleatórios entre 0 e 1
# np.random.randint(0, 10, (2, 2))  # inteiros entre 0 e 10 em matriz 2x2




# #   np.where()
# # Condicional em arrays:


# a = np.array([1, 2, 3, 4])
# np.where(a > 2, a, 0)  # substitui valores <= 2 por 0
