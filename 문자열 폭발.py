string = input()
boom = input()
while boom in string:
    string = string.replace(boom,'')
if string != '':
    print(string)
else:
    print('FRULA')