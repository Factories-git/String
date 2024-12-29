j = int(input())
arr = str(j)
le = set(arr)
num_arr = [i for i in le]
answer = [0 for i in range(len(le))]
answer2 = []
for i in arr:
    if len(answer2) == 0:
        continue
    if answer2[-1] == i:
        answer[num_arr.index(i)] += 1
        answer2.append(i)
    elif answer2[-1] != i:
        answer2.pop()
    print(answer2)
print(answer)