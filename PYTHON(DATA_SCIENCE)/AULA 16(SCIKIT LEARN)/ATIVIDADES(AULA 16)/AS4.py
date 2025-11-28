from sklearn.linear_model import LinearRegression
import numpy as np


pro = {

50:2.0,
100:3.5,
150:4.8,
200:5.5,
250:6.0



}




fertilizante_kg = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)
producao_ton = np.array([2.0, 3.5, 4.8, 5.5, 6.0])
    

modelo = LinearRegression()
modelo.fit(fertilizante_kg,producao_ton)

prox_mes = 6
producao_prevista = modelo.predict([[prox_mes]])[0]

print(round(producao_prevista))