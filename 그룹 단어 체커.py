import sys

input = sys.stdin.readline


re = 0
for _ in range(int(input())):
    isGroup = True
    s = input()
    stack = []
    counter = {}
    for i in s:
        if not stack or (counter.get(i) is None):
            stack.append(i)
            counter[i] = 1
            continue
        if counter[i] >= 1 and stack[-1] != i:
            isGroup = False
        else:
            stack.append(i)
            counter[i] += 1
    if isGroup:
        re += 1
print(re)