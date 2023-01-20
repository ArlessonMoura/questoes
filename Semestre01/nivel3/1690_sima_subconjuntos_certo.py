def encontre_menor_subset_sum(t, teste_cases):
    for i in range(t):
        n = teste_cases[i][0]
        arr = teste_cases[i][1]
        
        arr.sort()
        subset_sum = 1
        for j in range(n):
            if arr[j] > subset_sum:
                break
            subset_sum += arr[j]
        
        print(subset_sum)

t = int(input())
teste_cases = []
for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    teste_cases.append((n, arr))
encontre_menor_subset_sum(t, teste_cases)

"""
O algoritmo funciona da seguinte maneira:

1 - Ele lê a entrada T e todos os casos de teste de acordo com as especificações dadas.
2 - Para cada caso de teste:
    2.1 - Ele ordena o array de entrada.
    2.2 - Inicializa uma variável "subset_sum" com o valor
3 - Para cada elemento "x" no array:
    3.1 - Se "x" for maior do que "subset_sum", interromper o loop.
    3.2 - Adicione "x" a "subset_sum"
4 - Imprima o valor de "subset_sum"

"""