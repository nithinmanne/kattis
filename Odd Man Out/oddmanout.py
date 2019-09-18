from collections import defaultdict as ddict
N = int(input())
for i in range(N):
    input()
    g = ddict(lambda:0)
    for j in map(int, input().split()):
        g[j] += 1
    
    print(f'Case #{i+1}:', end=' ')
    for j in g:
        if g[j]==1: print(j)