n = int(input())
skeep = input()
skeep = skeep.replace('skeep', '?')
skeep_c = skeep.count('?')
c = skeep_c
s_s = s = ('skeep','skee?','ske?p','ske??','sk?ep','sk?e?','sk??p','sk???','s?eep','s?ee?','s?e?p','s?e??','s??ep','s??e?','s???p','s????')
for i in s_s:
    c += skeep.count(i)
print(c)