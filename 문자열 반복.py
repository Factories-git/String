for i in range(int(input())):
    n,s = map(str, input().split())
    n = int(n)
    s = list(map(lambda x : x*n, s))
    print(''.join(s))