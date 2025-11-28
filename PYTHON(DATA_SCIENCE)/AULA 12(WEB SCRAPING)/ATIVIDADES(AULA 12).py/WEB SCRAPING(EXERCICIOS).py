from bs4 import BeautifulSoup
import requests
import pandas as pd
import matplotlib.pyplot as plt



html = 'https://tabelatest.netlify.app/'
resp = requests.get(html)
html_content = resp.text


soup =  BeautifulSoup(html_content, 'html.parser')
tabela = soup.find('table')


# print(tabela)



# for headin in tabela.find_all('th'):
#     print(headin)



row_l = []
for linhas  in tabela.find_all('tr')[1:]:
    pass
    for dados in linhas.find_all('td')[3]:
        pass
    row_l.append(dados.get_text(strip=True))
print(row_l)


# for th in tabele         




# for i in table
