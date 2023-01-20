def testePrefixoUmAUm(item1, item2):
    # print('item1, item2')
    # print(item1, item2)
    if(len(item2) <= len(item1)):
        if(item2 in item1[:len(item2)]):
            return True
    elif(len(item1) <= len(item2)):
        if (item1 in item2[:len(item1)]):
            return True
    # print('False')
    return False


n = int(input())
lista = []
prefixo = 0
for cada in range(n):
    lista.append(input())
    if(cada > 0):
        for indexItem in range(len(lista)-1):
            if prefixo:
                break
            if (testePrefixoUmAUm(lista[indexItem], lista[-1])):
                prefixo = 1
                break

if prefixo:
    print('Conjunto Ruim')
else:
    print('Conjunto Bom')
