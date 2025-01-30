n = int(input())
compare = list(input())
re = 0
for i in range(n-1):
    tar = compare.copy()
    word = input()

    cnt = 0
    for w in word:
        if w in tar:
            tar.remove(w)
        else:
            cnt += 1

    if cnt < 2 and len(tar) < 2:
        re += 1
print(re)