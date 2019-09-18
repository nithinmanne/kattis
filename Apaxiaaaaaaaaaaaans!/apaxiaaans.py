inp = input()
out = ['']
for i in inp:
    if out[-1]!=i: out.append(i)
print(''.join(out))