import pandas as pd
dados = pd.read_csv('AULA 14(EXPORTACAO DE PANDAS)/aula.csv')

print(dados)

#dados.to_json('AULA 14(EXPORTACAO DE PANDAS)/aula.json')

#dados.to_excel('AULA 14(EXPORTACAO DE PANDAS)/aula.xlsx')

#s = dados.to_dict() = DICIONARIO

dados.to_html('AULA 14(EXPORTACAO DE PANDAS)/aula.html')