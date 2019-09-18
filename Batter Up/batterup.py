n = int(input().strip())
a = list(map(int, input().strip().split()))
s = 0

for i in a:
    if i == -1: n -= 1
    else: s+= i

print(s/n)