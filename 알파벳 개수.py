alpha = 'abcdefghijklmnopqlstuvwxyz'
s = input().lower()
c = []
for i in alpha:
    c.append(s.count(i))
print(' '.join(map(str, c)))