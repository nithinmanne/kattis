def hs(n):
    if n==1: return n
    elif n%2==1: return n+hs(3*n+1)
    else: return n+hs(n//2)
print(hs(int(input())))