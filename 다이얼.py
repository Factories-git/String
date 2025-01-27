def classfication(s):
    num = 0
    unicode = ord(s.lower())
    if 97 <= unicode <= 99:
        num = 2
    elif 100 <= unicode <= 102:
        num = 3
    elif 103 <= unicode <= 105:
        num = 4
    elif 106 <= unicode <= 108:
        num = 5
    elif 109 <= unicode <= 111:
        num = 6
    elif 112 <= unicode <= 115:
        num = 7
    elif 116 <= unicode <= 118:
        num = 8
    elif 119 <= unicode <= 122:
        num = 9
    return num


time = 0
dial = input().lower()
for i in dial:
    n = classfication(i)
    time += n + 1
print(time)