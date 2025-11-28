import matplotlib.pyplot as plt 
import pandas as pd

dados = pd.read_csv('DataSete/Exercicio2.csv')
df  =  pd.DataFrame(dados)

plt.figure(figsize=(6,6))
plt.bar(df['Mes'], df['Medias_Jose'] )
plt.title('____Medias de Jose____')
plt.show()