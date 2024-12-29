import sys

input = sys.stdin.readline
t = int(input())
for _ in range(t):
    s = input().strip()
    prevS = start = 0
    prevE = end = len(s) - 1
    answer = 0
    check = [False] * 2
    while start < end:
        if s[start] < end:
            start += 1
            end -= 1
        elif not any(check) and s[start+1] == s[end]:
            prevS = start
            prevE = end - 1
            answer = 1
            start += 1
            check[0] = True
        elif not any(check) and s[start] == s[end -1]:
            prevS = start + 1
            prevE = end
            answer = 1
            end -= 1
            check[1] = True
        else:
            if not any(check):
                answer = 2
                break
            if not check[0] or not check[1]:
                start = prevS
                end = prevE
                check[0] = check[1] = True
                continue

            answer = 2
            break
    print(answer)

