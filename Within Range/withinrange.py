x, c, r = map(int, input().split())
if x <= c+r and x >= c-r: print('True')
else: print('False')