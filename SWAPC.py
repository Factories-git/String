n = int(input())
s = input()
re = []
pass_ = set()
for j, i in enumerate(s):
    if i != 'P' and i != 'C' or len(re) == 0:
        re.append(i)
    else:
        if j not in pass_:
            if re[-1] == 'P' and i == 'C':
                pass_.add(j + 1)
                re.pop()
                re.append('C')
                re.append('P')
            elif re[-1] == 'C' and i == 'P':
                pass_.add(j+1)
                re.pop()
                re.append('P')
                re.append('C')
            else:
                re.append(i)
        else:
            re.append(i)
print(''.join(re))