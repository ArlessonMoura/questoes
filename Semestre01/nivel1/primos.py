# -*- coding: utf-8 -*-

def eh_primo(x):
    for i in range(2, x//2 + 1):
        if x % i == 0:
            return f'%d nao eh primo' % x
    return f'%d eh primo' % x


n = int(input())
for i in range(n):
    x = int(input())
    print(eh_primo(x))
    
