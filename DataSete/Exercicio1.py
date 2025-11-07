# EXERCICIO 1:

# dados.csv

# Nome,Idade,Cidade
# Ana,25,São Paulo
# João,30,Rio de Janeiro
# Maria,22,Belo Horizonte
# Carlos,35,Porto Alegre

# Crie um csv, e faça um analise baseada nos dados oferecidos.

# 1 - # Lendo o arquivo CSV
# 2 - # crie um dataFrame
# 3 - # calcule a média de idade
# 4 - # mediana de idade
# 5 - # busque os dados da Maria 
# 6 - # verifique as informações tecnicas do csv
# 7 - # traga descrição básica(estatistica)

# 8 - # agregação com o groupby()
#------------------------------------------------------------------------------
import pandas as pd

dados = pd.read_csv("DataSete/Exercicio.csv")
df = pd.DataFrame(dados)
print("DataFrame:")
print(df)

media_das_idades = df['Idade'].mean()
print("A Media das Idade:")
print(media_das_idades)

mediana_das_idades = df['Idade'].median()
print("A Mediana das Idade:")
print(mediana_das_idades)

dados_maria = df.groupby("Nome")[2]["Idade"][2]["Cidade"][2]
print("Os Dados de Maria:")
print(dados_maria)





