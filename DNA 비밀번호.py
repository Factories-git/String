myList = [0] * 4
check = 0


def myadd(s):
    global checkList, myList, check
    if s == 'A':
        myList[0] += 1
        if checkList[0] == myList[0]:
            check += 1
    if s == 'C':
        myList[1] += 1
        if checkList[1] == myList[1]:
            check += 1
    if s == 'G':
        myList[2] += 1
        if checkList[2] == myList[2]:
            check += 1
    if s == 'T':
        myList[3] += 1
        if checkList[3] == myList[3]:
            check += 1


def myremove(s):
    global checkList, myList, check
    if s == 'A':
        if checkList[0] == myList[0]:
            check -= 1
        myList[0] -= 1
    if s == 'C':
        if checkList[1] == myList[1]:
            check -= 1
        myList[1] -= 1
    if s == 'G':
        if checkList[2] == myList[2]:
            check -= 1
        myList[2] -= 1
    if s == 'T':
        if checkList[3] == myList[3]:
            check -= 1
        myList[3] -= 1


S, P = map(int, input().split())
Re = 0
a = list(input())
checkList = list(map(int, input().split()))

for i in range(4):
    if checkList[i] == 0:
        check += 1

for i in range(P):
    myadd(a[i])

if check == 4:
    Re += 1

for i in range(P, S):
    j = i - P
    myadd(a[i])
    myremove(a[j])
    if check == 4:
        Re += 1
print(Re)