n = int(input())

for i in range(n):
    t = input()
    list = []
    for j in t:
        if j == '(':
            list.append(j)
        
        elif j == ')':
            if len(list) != 0 and list[-1] == '(':
                list.pop()
                
            else:
                list.append(')')
    
    if len(list) == 0:
        print('YES')
        
    else:
        print('NO')        
    