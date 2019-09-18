C, n = map(int, input().split())

poss = True
tc = 0
for _ in range(n):
    l, e, s = map(int, input().split())
    
    if tc < l or tc + ( e - l ) > C or s * ( tc + ( e - l ) - C ) :
        poss = False
        break
    
    tc += (e - l)
    
if tc > 0 or s > 0: poss = False

if poss: print('possible')
else: print('impossible')