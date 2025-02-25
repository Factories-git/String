n = int(input())
s = list(input())
count = min(s.count('P'), s.count('C'))
pIndex = []
cIndex = []

for i in range(n):
    if s[i] == 'P':
        pIndex.append(i)
    elif s[i] == 'C':
        cIndex.append(i)

for i in range(count):
    p_idx = pIndex[i]
    c_idx = cIndex[i]
    s[p_idx], s[c_idx] = s[c_idx], s[p_idx]
print(''.join(s))