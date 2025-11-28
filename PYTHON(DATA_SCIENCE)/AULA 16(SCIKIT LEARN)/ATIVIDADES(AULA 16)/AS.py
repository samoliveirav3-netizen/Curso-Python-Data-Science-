from sklearn.linear_model import LinearRegression
import numpy as np


m = {

2:5.0,
4:6.5,
6:7.8,
8:8.5,
10:9.2



}




horas_estudo = np.array([1,2,3,4,5]).reshape(-1, 1)
notas = np.array([5.0, 6.5, 7.8, 8.5, 9.2])

    

modelo = LinearRegression()
modelo.fit(horas_estudo,notas)

prox_mes = 6
nota_prevista = modelo.predict([[prox_mes]])[0]
if nota_prevista <0:
    print(0)
elif nota_prevista >10:
    print(10)    
else:
    print(round(nota_prevista))