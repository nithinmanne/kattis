p, q = map(int, input().split())
while q != 0:
    m = p//q
    p -= m*q
    print(f'{m} {p} / {q}')
    p, q = map(int, input().split())