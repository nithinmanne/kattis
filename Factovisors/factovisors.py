import sys, math
from collections import defaultdict as ddict
for i in sys.stdin:
    a, b = map(int, i.strip().split())
    tb, f= b, ddict(lambda:0)
    for j in range(2,int(math.sqrt(b))+1):
        while tb%j==0:
            f[j]+=1
            tb /= j
    if tb != 1: f[tb]+=1
    for j in f:
        tj, c = j, 0
        while tj > 1 and tj <= a:
            c += a//tj
            tj *= j
        if c < f[j]:
            print(f'{b} does not divide {a}!')
            break
    else: print(f'{b} divides {a}!')