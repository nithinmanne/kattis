m1 = int(input())
b1 = int(input())
n = int(input())
outcomes = list(map(int, input().split()))

mi = m1
bi = b1
for outcome in outcomes:
    if outcome:
        mi += bi
        bi = min(b1, mi)
    else:
        mi -= bi
        bi = min(2*bi, mi)
    if mi==0: break
if mi: print(mi)
else: print('BROKE')
    