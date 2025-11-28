import statistics
def m_moda(nota):
 moda = statistics.mode(nota)
 con = set(nota)
 if len(nota) == len(nota):
   print('não tem moda')
 else:
   print('Moda:', moda)
def m_mediana(nota):
 mediana = statistics.median(nota)
 print('Mediana:', mediana)
def m_media(nota):
 media = statistics.mean(nota)
 print('Media:', media)
def m_varianca(nota):
 variancia = statistics.variance(nota)
 print("Variância: ",variancia)
def m_desvio_padrao(nota):
 desvio_padrao = statistics.stdev(nota)
 print("Desvio Padrao:",desvio_padrao)
def m_mn(nota):
 maior_nota = max(nota)
 print("Maior Nota:",maior_nota)
def m_men(nota):
 menor_nota = min(nota)
 print("Menor Nota:",menor_nota)

