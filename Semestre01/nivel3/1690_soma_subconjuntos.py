from itertools import combinations


def testeLista(menorNumero, listaOrdenada, pararJaAchou, usemosUsamdos):
    for item1 in listaOrdenada:
        if (item1 > menorNumero):
            voltasNosUsados = 1
            [usemosUsamdosAjustada, voltasNosUsados] = gerarNovaLista(
                voltasNosUsados, usemosUsamdos)
            [menorNumero, listaOrdenada, pararJaAchou, usemosUsamdos] = testeLista(
                menorNumero, usemosUsamdosAjustada, pararJaAchou, usemosUsamdos)
            pararJaAchou = True
            break
        else:
            usemosUsamdos.append(item1)
            menorNumero = item1 + 1
    return [menorNumero, listaOrdenada, pararJaAchou, usemosUsamdos]


def gerarNovaLista(voltasDadas, listaNumeros):
    voltasDadas += 1
    novaListaSemSoma = list(map(list, combinations(listaNumeros, voltasDadas)))
    listaSomada = []
    for cada in range(len(novaListaSemSoma)):
        listaSomada.append(sum(novaListaSemSoma[cada]))
    listaSomada.sort()
    return [listaSomada, voltasDadas]


def loopVerificacao(voltasDadas, listaOrdenada, listaNumeros, ultimoLista, menorNumero, pararJaAchou, usemosUsamdos):
    if(menorNumero == ultimoLista + 1):
        [listaOrdenada, voltasDadas] = gerarNovaLista(
            voltasDadas, listaNumeros)

        [menorNumero, listaOrdenada, pararJaAchou, usemosUsamdos] = testeLista(
            menorNumero, listaOrdenada, pararJaAchou, usemosUsamdos)
        if not (pararJaAchou):
            if (len(listaOrdenada) > 1):
                # print('listaOrdenada')
                # print(listaOrdenada)
                ultimoLista = int(listaOrdenada[-1])
                menorNumero = loopVerificacao(voltasDadas, listaOrdenada,
                                              listaNumeros, ultimoLista, menorNumero, pararJaAchou, usemosUsamdos)
    return menorNumero


contador = 0
quantidadeTestes = int(input())
while True:
    contador += 1
    usemosUsamdos = []
    if(contador > quantidadeTestes):
        break
    tamanhoLista = int(input())
    listaJunta = input()
    lista = listaJunta.split(' ')
    listaNumeros = list(map(int, lista))
    listaNumeros.sort()
    menorNumero = 1
    ultimoLista = 0
    voltasDadas = 0
    pararJaAchou = False
    menorNumero = loopVerificacao(voltasDadas, listaNumeros,
                                  listaNumeros, ultimoLista, menorNumero, pararJaAchou, usemosUsamdos)
    print(menorNumero)
