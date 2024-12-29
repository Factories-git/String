n = int(input())
s = input()
left = 0
right = n-1
while left < right:
    if s[left] != s[right] and s[left] != '?' and s[right] != '?':
        print(0)
        exit(0)
