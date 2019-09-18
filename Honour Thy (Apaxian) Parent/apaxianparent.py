Y, P = input().split()
if Y[-1] == 'e': ans = Y+'x'+P
elif Y[-1] in ['a','i','o','u']: ans = Y[:-1]+'ex'+P
elif Y[-2:] == 'ex': ans = Y+P
else: ans = Y+'ex'+P
print(ans)