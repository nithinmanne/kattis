def exp(x, n):
    if n == 0: return 1
    elif n == 1: return x
    elif n%2 == 0: return exp(x*x, n/2)
    elif n%2 == 1: return x*exp(x*x, (n-1)/2)
print(exp(*map(int, input().split())))