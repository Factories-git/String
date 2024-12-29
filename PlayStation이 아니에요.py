n = int(input())
stri = list(input())
if len(stri) == 1:
    print(''.join(stri))
    exit(0)
st = [stri[0],stri[1]]
for i in range(2,len(stri)):
    if st[-2] + st[-1] == 'PS' and (stri[i] == '4' or stri[i] == '5'):
        continue
    st.append(stri[i])
print(''.join(st))