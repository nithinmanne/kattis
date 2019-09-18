x, y = map(int, input().split())
output = []
for _ in range(x): output.append([0]*y)
for i in range(x):
    inl = input().split()
    for j in range(y):
        if inl[j] == '1':
            output[i][j] = 'X'
            if i+1<x:
                if j+1<y:
                    try: output[i+1][j+1] += 1
                    except: pass
                try: output[i+1][j] += 1
                except: pass
                if j-1>=0:
                    try: output[i+1][j-1] += 1
                    except: pass
            if j+1<y:
                try: output[i][j+1] += 1
                except: pass
            if j-1>=0:
                try: output[i][j-1] += 1
                except: pass
            if i-1>=0:
                if j+1<y:
                    try: output[i-1][j+1] += 1
                    except: pass
                try: output[i-1][j] += 1
                except: pass
                if j-1>=0:
                    try: output[i-1][j-1] += 1
                    except: pass
for i in output:
    print(''.join(map(lambda x: '-' if x==0 else str(x), i)))