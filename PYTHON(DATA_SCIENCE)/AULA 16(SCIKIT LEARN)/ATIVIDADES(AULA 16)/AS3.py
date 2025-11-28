from sklearn.linear_model import LinearRegression
import numpy as np


p = {

10:5,
20:12,
30:18,
40:25,
50:30



}




dias = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)
altura_cm = np.array([5, 12, 18, 25, 30])
    

modelo = LinearRegression()
modelo.fit(dias,altura_cm)

prox_mes = 6
altura_prevista = modelo.predict([[prox_mes]])[0]

print(round(altura_prevista))