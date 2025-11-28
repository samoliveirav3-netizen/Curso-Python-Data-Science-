from sklearn.linear_model import LinearRegression
import numpy as np


a = {

15:120,
20:100,
25:90,
30:110,
35:150



}




temperaturas = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)
consumo_kwh = np.array([120, 100, 90, 110, 150])

    

modelo = LinearRegression()
modelo.fit(temperaturas,consumo_kwh)

prox_mes = 6
consumo_prevista = modelo.predict([[prox_mes]])[0]


print(round(consumo_prevista))