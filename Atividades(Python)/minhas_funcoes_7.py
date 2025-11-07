import statistics
def m_moda(em3):
 moda = statistics.mode(em3)
 
 con = set(em3)
 if len(em3) == len(con):
  print('não tem moda')
 else:
  print('Moda:',moda)
def m_mediana(em3):
 mediana = statistics.median(em3)
 print('Mediana:', mediana)
def m_media(em3):
 media = statistics.mean(em3)
 print('Media:',media)
def m_varianca(em3):
 variancia = statistics.variance(em3)
 print("Variância: ",variancia)
def m_desvio_padrao(em3):
 desvio = statistics.stdev(em3)
 print("Desvio Padrao: ",desvio)
def m_amplitude(em3):
 amplitude = max(em3) - min(em3)
 print("Amplitude:",amplitude)