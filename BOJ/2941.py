croatia_list = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
text = input()

for i in croatia_list:
    text = text.replace(i, '*')
print(len(text))