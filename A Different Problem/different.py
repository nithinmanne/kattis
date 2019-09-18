import sys
for i in sys.stdin: print(next(map(lambda x:abs(x[0]-x[1]), [list(map(int, i.strip().split()))])))