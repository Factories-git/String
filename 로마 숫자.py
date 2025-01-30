n1 = input()
n2 = input()
eng_to_num = {'I' : '1 ', 'V' : '5 ', 'X' : "10 ", 'L' : "50 ", 'C' : "100 ", 'D' : "500 ", 'M' : "1000 "}
for e, n in eng_to_num.items():
    if e in n1:
        n1 = n1.replace(e, n)
    if e in n2:
        n2 = n2.replace(e, n)

real_n1 = 0
real_n2 = 0
pass_1 = set()
pass_2 = set()
n1 = list(map(int, n1.split()))
n2 = list(map(int, n2.split()))

for i in range(len(n1)-1):
    if i not in pass_1:
        if n1[i] < n1[i+1]:
            real_n1 += (n1[i+1] - n1[i])
            pass_1.add(i+1)
        else:
            real_n1 += n1[i]

for i in range(len(n2)-1):
    if i not in pass_2:
        if n2[i] < n2[i+1]:
            real_n2 += (n2[i+1] - n2[i])
            pass_2.add(i+1)
        else:
            real_n2 += n2[i]
if len(n1)-1 not in pass_1:
    real_n1 += n1[-1]
if len(n2)-1 not in pass_2:
    real_n2 += n2[-1]

int_bout = real_n1 + real_n2
print(int_bout)
str_bout = ''
for idx, i in enumerate(str(int_bout)):
    str_bout += (i + (len(str(int_bout)) - idx - 1) * '0')
    str_bout += ' '