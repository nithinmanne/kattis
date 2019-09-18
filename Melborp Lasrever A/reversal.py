def R(s): return s[0] if len(s)==1 else R(s[1:])+s[0]
print(R(input()))