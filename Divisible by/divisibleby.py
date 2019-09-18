m, n, p, q = map(int, input().split())
print(sum(filter(lambda x: x%p==0 and x%q==0, range(m, n+1))))