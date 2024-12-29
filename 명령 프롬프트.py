pattern = set()
l = []
n = int(input())
for i in range(n):
    s = input()
    l.append(s)

r = []
for i in range(len(l[0])):
    t_l = []
    for j in range(n):
        t_l.append(l[j][i])
    true_set = set(t_l)
    if len(true_set) == 1:
        r.append(l[0][i])
    else:
        r.append('?')
print(''.join(r))