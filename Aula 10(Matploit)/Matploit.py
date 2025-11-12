#Matploit
# Gráficos são representações visuais de dados, como coluna, linha, pizza e área.  desempenham um papel essencial no cotidiano, sendo encontrados em jornais revistas e internet. Sua compreensão é fundamental, especialmente em exames como concursos, vestibulares e Enem, que frequentemente os utilizam.
# Gráficos são representações visuais de dados, como coluna, linha, pizza e área.  desempenham um papel essencial no cotidiano, sendo encontrados em jornais revistas e internet.
# Sua compreensão é fundamental, especialmente em exames como concursos, vestibulares e Enem, que frequentemente os utilizam.

import matplotlib.pyplot as plt
import numpy as np
# fig, ax = plt.subplots()             
# ax.plot([1, 2, 3, 4], [1, 4, 2, 3])  
# plt.show()
 


# x = ['a','b','c','d','e','f','g']
# y = [1,22,30,10,55,10,15]


# plt.title('Isso é um titulo')
# plt.plot(x,y, color = 'orange', linewidth=3, marker='o')
# plt.bar(x,y)
# plt.grid(True)
# plt.xlabel('Nomes')
# plt.ylabel('Notas')
# plt.legend('xy')
# plt.show()
x = ["MÊS_1","MÊS_2","MÊS_3","MÊS_4"]
y = [[150,200,300],[300,250,300],[15,20,300],[150,2000,300000]]
MÊS_1 = y[0]
MÊS_2 = y[1]
MÊS_3 = y[2]
MÊS_4 = y[3]

plt.title("Grafico de Vendas")
plt.plot([MÊS_1],[0], color = "black")
plt.xlabel("Letras")
plt.ylabel("Numeros")
plt.legend("Teste", edgecolor = "red")
plt.show()