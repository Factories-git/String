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
num_to_rome = {
    '3000': 'MMM', '2000': 'MM', '1000': 'M',
    '900': 'CM', '800': 'DCCC', '700': 'DCC', '600': 'DC', '500': 'D', '400': 'CD',
    '300': 'CCC', '200': 'CC', '100': 'C',
    '90': 'XC', '80': 'LXXX', '70': 'LXX', '60': 'LX', '50': 'L', '40': 'XL',
    '30': 'XXX', '20': 'XX', '10': 'X',
    '9': 'IX', '8': 'VIII', '7': 'VII', '6': 'VI', '5': 'V', '4': 'IV',
    '3': 'III', '2': 'II', '1': 'I'
}
for n, e in num_to_rome.items():
    if n in str_bout:
        str_bout = str_bout.replace(n, e)
print(''.join(str_bout.split()))