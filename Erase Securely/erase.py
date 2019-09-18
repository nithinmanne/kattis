n = int(input())%2
a = input()
b = input()
out = 'succeeded'
if n:
    for i in range(len(a)):
        if a[i]==b[i]:
            out='failed'
            break
else:
    if a!=b: out='failed'
print('Deletion', out)