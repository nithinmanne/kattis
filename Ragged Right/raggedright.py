from sys import stdin
inp = []
for i in stdin: inp.append(i)
n = len(max(inp, key=len))
print(sum(map(lambda x: (n-len(x))**2, inp[:-1])))