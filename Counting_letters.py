line_voina = ''
for line in open('voyna-i-mir.txt'):
    line_voina += line
print(len(line_voina))
lst_dict = {}
for x in line_voina:
    lst_dict.setdefault(x, 0)
    lst_dict[x] += 1

print(lst_dict)
print('*'*10)
s = sorted(list(lst_dict.items()))
print(s)
