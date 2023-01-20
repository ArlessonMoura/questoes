from threading import Thread


def loopAddFragmentos(entrada, tamanhoSegmento, contadores, tamanhoLista):
    print('inicio loopAddFragmentos')
    print(entrada, tamanhoSegmento, contadores, tamanhoLista)
    for varrendo in range(tamanhoLista-tamanhoSegmento):
        itemAdd = entrada[varrendo:varrendo+tamanhoSegmento]
        print('itemAdd')
        print(itemAdd)
        if not itemAdd in contadores[0]:
            contadores[0].append(itemAdd)
            contadores[1].append(0)
        else:
            index = contadores[0].index(itemAdd)
            if contadores[1][index] == 0:
                contadores[1][index] += 1


def teste():
    print('oiiii')


while True:
    entrada = input()
    if(entrada == '*'):
        break
    tamanhoLista = len(entrada)
    if(tamanhoLista == 1):
        print(0)
    else:
        contadores = [[], []]
        processos = []
        lista = range(tamanhoLista // 2)
        print('lista')
        print(lista)

        for tamanhoSegmento in lista:
            print('tamanhoSegmento')
            print(tamanhoSegmento)
            processos[tamanhoSegmento] = Thread(target=print, args=[1])
            # 1, entrada, tamanhoSegmento, contadores, tamanhoLista
            # processos[tamanhoSegmento].start()
        for tamanhoSegmento in lista:
            # processos[tamanhoSegmento].join()
            print('contadores')
        print(contadores)
        print(sum(contadores[1]))
