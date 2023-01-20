from itertools import combinations


def testeLista(menorNumero, listaOrdenada):
    for item1 in listaOrdenada:
        if (item1 > menorNumero):
            break
        else:
            menorNumero = item1 + 1
    return menorNumero


def gerarNovaLista(listaNumeros):
    numbers = listaNumeros
    comb = []
    for r in range(len(numbers)+1):
        for combination in combinations(numbers, r):
            comb.append(combination)
    listaSomada = []
    for cada in range(len(comb)):
        listaSomada.append(sum(comb[cada]))
    listaSomada.sort()
    return [listaSomada]


def loopVerificacao(listaNumeros,  menorNumero):
    [listaOrdenada] = gerarNovaLista(listaNumeros)
    menorNumero = testeLista(menorNumero, listaOrdenada)
    return menorNumero


contador = 0
quantidadeTestes = int(input())
teste_cases = []
for i in range(quantidadeTestes):
    contador += 1
    if(contador > quantidadeTestes):
        break
    tamanhoLista = int(input())
    listaJunta = input()
    lista = listaJunta.split(' ')[0:tamanhoLista]
    listaNumeros = list(map(int, lista))
    menorNumero = 1
    menorNumero = loopVerificacao(listaNumeros, menorNumero)
    print(menorNumero)
