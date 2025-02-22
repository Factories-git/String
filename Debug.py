from collections import deque
s = input()
st = []
for i in range(len(s)-1, -1, -1):
    st.append(s[i])
    if len(st) >= 2:
        if st[-1] == 'W' and st[-2] == 'A':
            st[-1] = 'A'
            st[-2] = 'C'
print(''.join(st[::-1]))