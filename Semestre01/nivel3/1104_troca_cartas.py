/home/cleydson/Documentos/sistemas/Sistemas/estudoPython/Semestre01/nivel3/1104_troca_cartas.py
while True:
    quantidadeCartasAB = input()
    if(quantidadeCartasAB == '0 0'):
        break
    cartasAJuntas = input()
    cartasBJuntas = input()

    cartasAComDuplicacao = cartasAJuntas.split(' ')
    cartasBComDuplicacao = cartasBJuntas.split(' ')

    cartasA = list(dict.fromkeys(cartasAComDuplicacao))
    cartasB = list(dict.fromkeys(cartasBComDuplicacao))

    quantidadeA = len(cartasA)
    quantidadeB = len(cartasB)

    intersecao = list(set(cartasA) & set(cartasB))
    quantidadeIntersecao = len(intersecao)
    quantidadeASemB = quantidadeA - quantidadeIntersecao
    quantidadeBSemA = quantidadeB - quantidadeIntersecao

    quantidadePermitidaTrocas = min(quantidadeASemB, quantidadeBSemA)
    print(quantidadePermitidaTrocas)
