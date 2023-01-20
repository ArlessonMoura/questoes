n = int(input())

hora = n // 3600
nSemHora = n - (hora * 3600)
minuto = nSemHora // 60
segundo = nSemHora - (minuto *60)

print('{}:{}:{}'.format(hora, minuto, segundo))