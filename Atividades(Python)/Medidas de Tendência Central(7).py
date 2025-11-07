#Varianca:
import statistics
dados = [23,4,5,46,4,7,8,9,1,3,34]
variancia = statistics.variance(dados)
print("Variância: ",variancia)
#Desvio Padrao:
desvio = statistics.stdev(dados)
print("Desvio Padrao: ",desvio)
#Amplitude:
amplitude = max(dados) - min(dados)
print("Amplitude:",amplitude)
