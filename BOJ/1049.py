# 기타줄 -> 그리디

n, m = map(int, input().split())

a_list = []
b_list = []

for i in range(m):
    a, b = map(int, input().split())
    a_list.append(a)
    b_list.append(b)

a_list.sort()
b_list.sort()    

list = []

if n < 6:
    list.append(a_list[0])
    list.append(b_list[0]*n)
    
else:
    list.append((n//6+1)*a_list[0])
    list.append((n//6)*a_list[0] + (n%6)*b_list[0])
    list.append(n*b_list[0])
     
print(min(list)) 
