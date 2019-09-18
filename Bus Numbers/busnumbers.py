input()
buses = sorted(map(int, input().split()))
fb = lb = buses[0]
for cb in buses[1:]:
    if cb == lb + 1:
        lb = cb
        if cb == buses[-1]:
            if lb - fb == 1: print(f'{fb} {cb}', end=' ')
            else: print(f'{fb}-{cb}', end=' ')
    else:
        if fb == lb: print(f'{fb}', end=' ')
        elif lb - fb == 1: print(f'{fb} {lb}', end=' ')
        else: print(f'{fb}-{lb}', end=' ')
        fb = lb = cb
        if cb == buses[-1]: print(f'{cb}', end=' ')