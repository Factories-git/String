from collections import Counter

n = int(input())
compare = input()
le_com = len(compare)
set_c = set(compare)
re = 0
for i in range(n-1):
    s = list(input())
    if not -1 <= le_com - len(s) <= 1:
        continue
    c = Counter(s)
    set_s = set(s) - set_c
    if len(set_s) > 1:
        continue
    if not set_s:
        re += 1
        continue
    set_s = list(set_s)
    if c[set_s[0]] == 1:
        re += 1
print(re)