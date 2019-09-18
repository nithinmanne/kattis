inp = input()
def palin(inp):
    if len(inp)==1: return True
    elif len(inp)==2: return inp[0]==inp[1]
    else: return inp[0]==inp[-1] and palin(inp[1:-1])
if palin(inp): print('PALINDROME')
else: print('NOT PALINDROME')