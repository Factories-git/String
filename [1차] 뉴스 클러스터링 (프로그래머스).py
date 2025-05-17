def my_intersection(a1, a2):
    a = []
    for i in a1:
        if i in a2:
            a2.remove(i)
            a.append(i)
    return a

def my_union(a1, a2):
    a = a1[:]
    for i in a2:
        if i in a1:
            a1.remove(i)
        else:
            a.append(i)
    return a
def solution(str1, str2):
    answer = 0
    str1 = str1.lower()
    str2 = str2.lower()
    st_1 = []
    st_2 = []
    for i in range(len(str1)-1):
        sliding_w = str1[i:i+2]
        if sliding_w.isalpha():
            st_1.append(sliding_w)
    for i in range(len(str2)-1):
        sliding_w = str2[i:i+2]
        if sliding_w.isalpha():
            st_2.append(sliding_w)
    s_1 = my_intersection(st_1.copy(), st_2.copy())
    s_2 = my_union(st_1.copy(), st_2.copy())
    if not s_1 and not s_2:
        return 65536
    return int((len(s_1) / len(s_2)) * 65536)


print(solution('ababab', 'bababa'))