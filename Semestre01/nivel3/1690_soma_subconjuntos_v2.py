from itertools import combinations


def testeLista(menorNumero, listaOrdenada, pararJaAchou):
    for item1 in listaOrdenada:
        if (item1 > menorNumero):
            pararJaAchou = True
            break
        else:
            menorNumero += 1
    return [menorNumero, listaOrdenada, pararJaAchou]


def gerarNovaLista(voltasDadas, listaNumeros):
    voltasDadas += 1
    novaListaSemSoma = list(map(list, combinations(listaNumeros, voltasDadas)))
    listaSomada = []
    for cada in range(len(novaListaSemSoma)):
        listaSomada.append(sum(novaListaSemSoma[cada]))
    listaSomada.sort()
    return [listaSomada, voltasDadas]


def loopVerificacao(voltasDadas, listaOrdenada, listaNumeros, ultimoLista, menorNumero, pararJaAchou):
    if(menorNumero == ultimoLista + 1):
        [listaOrdenada, voltasDadas] = gerarNovaLista(
            voltasDadas, listaNumeros)

        [menorNumero, listaOrdenada, pararJaAchou] = testeLista(
            menorNumero, listaOrdenada, pararJaAchou)
        if not (pararJaAchou):
            ultimoLista = int(listaOrdenada[-1])
            menorNumero = loopVerificacao(voltasDadas, listaOrdenada,
                                          listaNumeros, ultimoLista, menorNumero, pararJaAchou)
    return menorNumero


contador = 0
quantidadeTestes = int(input())
while True:
    contador += 1
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
                                  listaNumeros, ultimoLista, menorNumero, pararJaAchou)
    print(menorNumero)
