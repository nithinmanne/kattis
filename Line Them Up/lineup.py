n = int(input())
inp = []
inp.append(input())
inp.append(input())
if inp[0] < inp[1]: order = 0
else: order = 1
flag = 0
for i in range(n-2):
    j = input()
    if order == 0:
        if inp[i+1] > j:
            flag = 1
            break
    else:
        if inp[i+1] < j:
            flag = 1
            break
    inp.append(j)
if flag:
    print('NEITHER')
elif order == 0:
    print('INCREASING')
else:
    print('DECREASING')
    