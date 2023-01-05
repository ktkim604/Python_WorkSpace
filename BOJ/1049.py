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

if ((n//6) + 1) * a[0] > (n//6) * a[0] + (n%6)*b[0]:
    print((n//6) * a[0] + (n%6)*b[0])
    
else:
    print(((n//6) + 1) * a[0]) 

