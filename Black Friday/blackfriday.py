input()
o = {}
for i, j in enumerate(map(int, input().split())):
    if j in o: o[j] = -1
    else: o[j] = i
for i in sorted(o, reverse=True):
    if o[i] != -1:
        print(o[i]+1)
        break
else:
    print('none')