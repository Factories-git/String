n = int(input())
dict = {'bigdata' : '0', 'security' : '0'}
s = input()
s = s.replace('bigdata', '0')
s = s.replace('security', '1')
print(s)
if s.count('1') < s.count('0'):
    print('bigdata?')
elif s.count('1') > s.count('0'):
    print('security!')
else:
    print('bigdata? security!')