import timeit
import numpy as np


def soma1 ():
    lista  =  [1,2,3]
    print(lista)
    return lista


soma1()
time = timeit.timeit(soma1, number=10)
print('função1', time)


def soma2():
      lista = np.array([1,2,3])
      print(lista)
      return lista 


time = timeit.timeit(soma2, number=10)
print('função2', time)


