from sklearn.linear_model import LinearRegression
import numpy as np

vendas = {

"Jan":2030,
"Fev":3200,
"Mar":4320


}

meses = np.array([1,2,3]).reshape(-1,1)
valores = np.array([2030,3200,4320])

modelo = LinearRegression()
modelo.fit(meses,valores)

prox_mes = 4
venda_prevista = modelo.predict([[prox_mes]])[0]

print(round(venda_prevista))