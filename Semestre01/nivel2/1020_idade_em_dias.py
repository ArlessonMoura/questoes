# uri 1020 python

totalDias = int(input('Escreva total de dias: '))

anos = totalDias // 365
restoDias = totalDias - (anos*365)

meses = restoDias // 30

soDias = restoDias - (meses*30)
print('{} anos(s)'.format(anos))
print('{} mes(s)'.format(meses))
print('{} dia(s)'.format(soDias))
