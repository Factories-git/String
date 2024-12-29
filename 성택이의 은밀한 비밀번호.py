import sys

for i in range(int(input())):
    s = sys.stdin.readline()
    length = len(s)
    if 6 <= length <= 9:
        print('yes')
    else:
        print('no')
