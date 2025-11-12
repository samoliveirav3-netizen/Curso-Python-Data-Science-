import matplotlib.pyplot as plt 
import pandas as pd


dados = pd.read_csv('DataSete/DadosdeVendas.csv')
df  =  pd.DataFrame(dados)

style =  {
'family':'arial',
'size':20,
'color':'red'
}

plt.figure(figsize=(6,6))



cores = ['yellow', 'green','blue']
# plt.text( df['vendas'],df['mes'], facecolor='red', alpha=0.5)
plt.pie(df['vendas'], labels=df['mes'], autopct= '%1.1f%%', colors= cores)
plt.xlabel('Vendas')
plt.ylabel('Lucro')
plt.title('DISTRIBUIÇÃO DE VENDAS POR MÊS ', fontdict=style)
plt.show()


plt.figure(figsize=(6,6))
plt.scatter(dados['vendas'],dados['lucro'])
plt.title('RELAÇÃO DE VENDAS POR LUCRO ')
plt.savefig('grafico_pizz.png')
plt.show()


plt.figure(figsize=(6,6))
plt.bar(df['mes'], df['vendas'] )
plt.title('VENDAS POR MÊS ')
plt.savefig('grafico_pizz.png')
plt.show()


plt.figure(figsize=(6,6))
plt.plot(df['mes'], df['lucro'] )
plt.title('EVOLUÇÃO DO LUCRO AO LONGO DOS MESES')
plt.savefig('grafico_pizz.png')
plt.show()










# x = ['a','b','c','d','e','f','g']
# y = [1,22,30,10,55,10,15]

# plt.title('Isso é um titulo')
# plt.plot(x,y, color = 'orange', linewidth=3, marker='o')
# plt.bar(x,y, color = 'red', linewidth=5, edgecolor = 'blue')
# plt.grid(True)
# plt.xlabel('Nomes')
# plt.ylabel('Notas')
# plt.legend('xy')
# plt.show()