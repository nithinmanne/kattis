def fill(a, N, i, v, x):
    if i < 0 or i >= N: return
    elif a[i] != v: return
    elif a[i] == x: return
    else:
        a[i] = x
        fill(a, N, i - 1, v, x)
        fill(a, N, i + 1, v, x)

N, i, x = map(int, input().strip().split())
a = list(map(int, input().strip().split()))

fill(a, N, i, a[i], x)

print(*a)