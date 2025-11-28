import sqlite3
import pandas as pd
import matplotlib.pyplot as plt 


conn = sqlite3.connect("Banco_Dados.db")
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS BANCO(



    NOMES TEXT,
    IDADE INTEGER,
    EMAIL TEXT

                          )



                      ''')




c.execute("INSERT INTO BANCO VALUES(?,?,?)",("SAMUEL",16,"samuel@gmail.com"))
conn.commit()

c.execute("INSERT INTO BANCO VALUES(?,?,?)",("LARISSA",40,"larrisa@gmail.com"))
conn.commit()

c.execute("INSERT INTO BANCO VALUES(?,?,?)",("CAIO",11,"caio@gmail.com"))
conn.commit()

c.execute("INSERT INTO BANCO VALUES(?,?,?)",("PEDRO",30,"pedro@gmail.com"))
conn.commit()

y = [
   ("A",20,"a@gmail.com"),
   ("B",20,"b@gmail.com"),
   ("C",20,"c@gmail.com"),
   ("D",20,"d@gmail.com"),
   ("E",20,"e@gmail.com"),
   ("F",20,"f@gmail.com"),
   ("G",20,"g@gmail.com"),
   ("H",20,"h@gmail.com")
]

c.executemany("INSERT INTO BANCO VALUES(?,?,?)",y)
conn.commit()

c.execute("SELECT * FROM BANCO")
dados = c.fetchall()

dicionario = {
"lista_nome" : [],
"lista_idade" : [],
"lista_email" : []
}
# print(dados)
for NOMES in dados:
    for nome in NOMES:
        dicionario["lista_nome"].append(NOMES[0])
        

for IDADE in dados:
    for idade in IDADE:
        dicionario["lista_idade"].append(IDADE[1])
        

for EMAIL in dados:
    for email in EMAIL:
        dicionario["lista_email"].append(EMAIL[2])

print(dicionario)
#DATAFREME
df = pd.DataFrame(dicionario)
df.to_csv('AULA 15(BANCO DE DADOS)/BD.csv')


#GRAFICO
plt.figure(figsize = (10,8))
plt.bar(df["lista_nome"],df["lista_idade"])
plt.title('NOMES E IDADES ')
# plt.savefig('grafico_pizz.png')
plt.show()



conn.close()