s = input()
left = 0
right = len(s) - 1
po = 0

while left < right:
    if s[left] == s[right]:
        po += 1
    left += 1
    right -= 1
print(1 if po == len(s)//2 else 0)
