# uri 1199 python

while True:
    n = input('')
    if(n and n[0] == '-'):
        break
    if(n and n[1] == 'x'):
        n = int(n, 16)
    else:
        n = hex(int(n))
        n = n[:2] + n[2:].upper()
    print(n)

    # break
    # if n == '-1':
    #     break
    #     if n.isdigit():
    #         n = hex(int(n))
    #         n = n[:2] + n[2:].upper()
    #     else:
    #         n = int(n, 16)
    #         print(n)
