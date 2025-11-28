# import seaborn as sns
# print(sns.get_dataset_names())

# ['anagrams', 'anscombe', 'attention', 'brain_networks', 'car_crashes', 'diamonds', 
#  'dots', 'dowjones', 'exercise', 'flights', 'fmri', 'geyser', 'glue', 'healthexp', 
#  'iris', 'mpg', 'penguins', 'planets', 'seaice', 'taxis', 'tips', 'titanic']


# import seaborn as sns
# import matplotlib.pyplot as plt
# import pandas as pd

# # datasets COM LABELS 
# tips = sns.load_dataset('titanic')
# iris = sns.load_dataset('iris')

# #  barras simples
# sns.barplot(x='sex', y='age', data=tips)
# plt.title('Conta média por dia da semana')
# plt.show()


# titanic =  sns.load_dataset('titanic')
# # Gráfico de BAR
# sns.barplot(x='sex', y='age', data=titanic, estimator='mean')
# plt.title('Média de Idade por Sexo (Titanic)')
# plt.xlabel('Sexo')
# plt.ylabel('Idade Média')
# plt.show()