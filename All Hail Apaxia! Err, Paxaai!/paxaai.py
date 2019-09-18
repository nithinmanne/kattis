nam = list(input())
i = 0
while(i+2<=len(nam)):
    nam[i:i+2]=[nam[i+1],nam[i]]
    i += 2
print(''.join(nam))