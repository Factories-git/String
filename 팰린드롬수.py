import sys

input = sys.stdin.readline

n = str(input()).split()[0]
if not n == 0:
    if len(str(n)) % 2 == 0:
        a = str(n)[:len(str(n)) // 2]
        b = str(n)[len(str(n)) // 2:]
        a = list(a)
        a.reverse()
        a = ''.join(a)
        check = 'no'
        if a == b:
            check = 'yes'
        print(check)
while True:
    n = input().split()[0]
    if n == '0':
        break
    if len(n) % 2 == 0:
        a = n[:len(n) // 2]
        b = str(n)[len(n) // 2:]
        check = 'no'
        if a == b:
            check = 'yes'
        print(check)