
from datetime import datetime
contadores = 0

casos = {
    "ababcabb": 3,
    "mississippi": 9,
    "aaaaaaaaaaaaaaaaaaaaaaaaaa": 25,
    "012345678,abcdefg.STUVWXYZ": 0,
    "say.twice,say.twice": 45,
}
usado = 0


def loopAddFragmentos(entrada, tamanhoLista):
    global contadores
    palavrasAchadas = []
    for i in range(tamanhoLista-1):
        for y in range(i+1, tamanhoLista):
            if i + y < tamanhoLista or True:
                palavaAchada = entrada[i:y]
                print(i, y)
                print(palavaAchada)
                print('  ')
                if(palavaAchada and entrada.find(palavaAchada, i+1) != -1 and not palavaAchada in palavrasAchadas):
                    contadores += 1
                    palavrasAchadas.append(palavaAchada)


while True:
    if usado > 4:
        entrada = input()
        valorEsperado = ''
    else:
        entrada = list(casos)[usado]
        valorEsperado = list(casos.values())[usado]
        usado += +1
        print('---------')
        espera = input('Usando Estudo de caso  ' + str(usado) +'   "' + entrada + '"   valor esperado: '+ str(valorEsperado))
    if(entrada == '*'):
        break
    tamanhoLista = len(entrada)
    if(tamanhoLista == 1):
        print(0)
    else:
        inicio = datetime.timestamp(datetime.now())
        loopAddFragmentos(entrada, tamanhoLista)
        termino = datetime.timestamp(datetime.now())
        print('Tempo: ', termino - inicio)
        print('--------Resultado-----------')
        print(contadores)
        if(valorEsperado != ''):
            print('--------Esperado-----------')
            print(valorEsperado)
        contadores = 0
