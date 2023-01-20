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