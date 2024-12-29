dic = {'NLCS' : 'North London Collegiate School', 'BHA' : 'Branksome Hall Asia', 'KIS' : 'Korea International School', 'SJA' : 'St. Johnsbury Academy'}
d = input()
for i,j in dic.items():
    if i == d:
        print(d.replace(i,j))
        exit(0)