word1 = sorted(input())
word2 = sorted(input())
c = 0
for i in range(len(word1)):
    if word1[i] not in word2:
        c += 2
print(c)