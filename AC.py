from collections import deque
import sys

input = sys.stdin.readline

t = int(input())
for i in range(t):
    p = input().strip()
    n = int(input().strip())
    arr = input().strip()
    if n > 0:
        arr = arr[1:-1]
        if arr:
            arr = arr.split(',')
        else:
            arr = []
    else:
        arr = []
    dq = deque(arr)
    re = False
    error = False
    for j in p:
        if j == 'D':
            if dq:
                if not re:
                    dq.popleft()
                else:
                    dq.pop()
            else:
                error = True
        elif j == 'R':
            re = not re
    if re:
        dq.reverse()
    if not error:
        print('[' + ','.join(dq) + ']')
    else:
        print('error')


