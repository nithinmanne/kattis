a, b, c = map(int, input().split())
if a > 31: format = 3
elif a > 12:
    if c > 31: format = 2
    else: format = 0
else:
    if b > 12: format = 1
    else: format = 0
if format: print(f'Format #{format}')
else: print('Ambiguous')