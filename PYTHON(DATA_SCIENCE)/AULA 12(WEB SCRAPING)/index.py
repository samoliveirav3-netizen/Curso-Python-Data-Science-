from bs4 import BeautifulSoup
import requests
import pandas as pd
import matplotlib.pyplot as plt

html =  'https://bea3853.github.io/teste_web/'
headers =  {'User-Agents':'Mozilla/5.0'}
resp = requests.get(html, headers=headers)
soup = BeautifulSoup(resp.text,'html.parser')

# print(soup)

nome  =  []
valores  =  []
avaliacao = []


# loop  for 
for produto in soup.find_all('div', class_ = 'produto'):
    nome.append(produto.find('h2').text)
    valores.append(float(produto.find('span', class_='preco').text.replace('R$','').replace('.','').replace(',','.')))
    avaliacao.append(int(produto.find('span', class_='avaliacao').text.replace('Avaliação', '').replace('-', '')))
    print(nome)
    print(valores)
    print(avaliacao)

# list compression 
# val   =  [float(produto.find('span', class_='preco').text.replace('R$','').replace('.','').replace(',','.')) 
#           for produto in soup.find_all('div', class_ = 'produto')]
# print(val)

# avaliacao =  [int(produto.find('span', class_ = 'avaliacao').text.replace('Avaliação', '').replace('-','')) 
#               for produto in soup.find_all('div', class_ = 'produto') ]
# print(avaliacao)

df = pd.DataFrame({
'Modelo':nome,
'Valores': valores,
'Avaliação':avaliacao
})

df.to_csv('dados.csv', index=False)
df = pd.read_csv('dados.csv')
df  =  pd.DataFrame(df)
print(df)

# criando um filtro 
df = df[df['Valores'] < 2500.0]
print(df)

# Preço por marca

preco_medio_maraca  =  df.groupby('Modelo')['Valores'].mean()
print(preco_medio_maraca)

plt.figure(figsize=(10,8))
plt.bar(df['Modelo'],df['Valores'])
plt.xlabel('Modelo')
plt.ylabel('Valores')
plt.title('Comparação de valores')
plt.show()
