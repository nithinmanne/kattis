N = int(input().strip())

xeq = set()
yeq = set()
xpyeq = set()
xmyeq = set()

correct = 1
for _ in range(N):
    x, y = map(int, input().strip().split())
    if x in xeq or y in yeq or (x+y) in xpyeq or (x-y) in xmyeq:
        correct = 0
        break
    xeq.add(x)
    yeq.add(y)
    xpyeq.add(x+y)
    xmyeq.add(x-y)

if correct: print('CORRECT')
else: print('INCORRECT')