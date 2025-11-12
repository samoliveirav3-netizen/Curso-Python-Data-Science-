import statistics
def m_moda1(frequencias,):
 moda = statistics.mode(frequencias)
 con = set(frequencias)
 if len(frequencias) == len(con):
  print('não tem moda')
 else:
  print('Moda:', moda)
def m_mediana1(frequencias):
 mediana = statistics.median(frequencias)
 print('Mediana:', mediana)
def m_media1(frequencias):
 media = statistics.mean(frequencias)
 print('Media:', media)

def m_moda2(frequencias1):
 moda = statistics.mode(frequencias1)
 con = set(frequencias1)
 if len(frequencias1) == len(con):
  print('não tem moda')
 else:
  print('Moda:', moda)
def m_mediana2(frequencias1):
 mediana = statistics.median(frequencias1)
 print('Mediana:', mediana)
def m_media2(frequencias1):
 media = statistics.mean(frequencias1)
 print('Media:', media)

def m_moda3(frequencias2):
 moda = statistics.mode(frequencias2)
 con = set(frequencias2)
 if len(frequencias2) == len(con):
  print('não tem moda')
 else:
  print('Moda:', moda)
def m_mediana3(frequencias2):
 mediana = statistics.median(frequencias2)
 print('Mediana:', mediana)
def m_media3(frequencias2):
 media = statistics.mean(frequencias2)
 print('Media:', media)
