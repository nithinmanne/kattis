from math import sqrt, ceil
for _ in range(int(input())):
    inp = list(input())
    L = len(inp)
    M = ceil(sqrt(L))
    inp += ['*']*(M*M-L)
    out = []
    for i in range(M):
        for j in range(M):
            out.append(inp[(M-j-1)*M+(i)])
    print(''.join(filter(lambda x: x!='*', out)))