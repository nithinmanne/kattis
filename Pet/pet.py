m, mi = 0, -1
for i in range(5):
    s = sum(map(int, input().split()))
    if s>m:
        m=s
        mi=i
print(f'{mi+1} {m}')