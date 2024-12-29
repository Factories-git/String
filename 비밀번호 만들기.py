s1 = input()
s2 = input()
password = []
for i in s1:
    if i in s2:
        password.append(i)
print(''.join(password))