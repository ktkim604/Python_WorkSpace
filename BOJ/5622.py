dial_list = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
t = input()

time = 0
for dial in dial_list:
    for i in dial:
        for j in t:
            if i == j:
                time += dial_list.index(dial) + 3
print(time)
                
    