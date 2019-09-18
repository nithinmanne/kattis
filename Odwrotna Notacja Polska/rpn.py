inp = input().split()
stk = []

err = ''
for i in inp:
    if i == 'true': stk.append(True)
    elif i == 'false': stk.append(False)
    elif i == '+':
        if len(stk) < 2:
            err = 'SYNTAX ERROR'
            break
        x = stk.pop()
        y = stk.pop()
        if type(x)==type(True) or type(y)==type(True):
            err = 'TYPE ERROR'
            break
        stk.append(x + y)
    elif i == '*':
        if len(stk) < 2:
            err = 'SYNTAX ERROR'
            break
        x = stk.pop()
        y = stk.pop()
        if type(x)==type(True) or type(y)==type(True):
            err = 'TYPE ERROR'
            break
        stk.append(x * y)
    elif i == '==':
        if len(stk) < 2:
            err = 'SYNTAX ERROR'
            break
        x = stk.pop()
        y = stk.pop()
        if type(x)==type(True) or type(y)==type(True):
            err = 'TYPE ERROR'
            break
        stk.append(x == y)
    elif i == 'and':
        if len(stk) < 2:
            err = 'SYNTAX ERROR'
            break
        x = stk.pop()
        y = stk.pop()
        if type(x)==type(1) or type(y)==type(1):
            err = 'TYPE ERROR'
            break
        stk.append(x and y)
    elif i == 'or':
        if len(stk) < 2:
            err = 'SYNTAX ERROR'
            break
        x = stk.pop()
        y = stk.pop()
        if type(x)==type(1) or type(y)==type(1):
            err = 'TYPE ERROR'
            break
        stk.append(x or y)
    else:
        stk.append(int(i))
if err!='': print(err)
else:
    if len(stk) != 1: print('SYNTAX ERROR')
    else:
        if stk[0] == True: print('true')
        elif stk[0] == False: print('false')
        else: print(stk[0])