input()
c, t = 0, 0
for i in map(int, input().split()):
    if i < 0: continue
    c += 1
    t += i
if c==0: print('INSUFFICIENT DATA')
else: print(t//c)