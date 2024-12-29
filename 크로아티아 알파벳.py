alpha_to_chro = {'c=' : '하', 'c-' : '하', 'dz=' : '하', 'd-' : '하', 'lj' : '하', 'nj' : '하', 's=' : '하', 'z=' : '하'}
string = input()
for chro,korean in alpha_to_chro.items():
    string = string.replace(chro,korean)
print(len(string))