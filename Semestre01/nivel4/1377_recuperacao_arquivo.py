from threading import Thread
from datetime import datetime

contadores = 0


def loopAddFragmentos(entrada, tamanhoSegmento, tamanhoLista):
    global contadores
    soma = 0
    contadoresInternos = []
    if(tamanhoSegmento == tamanhoLista):
        return
    for varrendo in range(tamanhoLista-tamanhoSegmento+1):
        itemAdd = entrada[varrendo:varrendo+tamanhoSegmento]
        if (itemAdd in contadoresInternos):
            continue
        posicao1 = entrada.find(itemAdd, varrendo+1)
        if posicao1 != -1:
            contadoresInternos.append(itemAdd)
            soma += 1
            continue
    contadores += soma


while True:
    entrada = input()
    if(entrada == '*'):
        break
    tamanhoLista = len(entrada)
    if(tamanhoLista == 1):
        print(0)
    else:
        inicio = datetime.timestamp(datetime.now())
        processos = []
        lista = range(tamanhoLista-1)
        for tamanhoSegmento in lista:
            # loopAddFragmentos(entrada, tamanhoSegmento+1, tamanhoLista)
            processos.append(Thread(
                target=loopAddFragmentos, args=(entrada, tamanhoSegmento+1, tamanhoLista)))
            processos[tamanhoSegmento].start()
        for tamanhoSegmento in lista:
            processos[tamanhoSegmento].join()
        print(contadores)
        termino = datetime.timestamp(datetime.now())
        print('Tempo: ', termino - inicio)
        contadores = 0
