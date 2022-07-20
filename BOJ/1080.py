n, m = map(int, input().split())

a = []
b = []

for i in range(2):
    for j in range(n):
        num = list(map(int, list(input())))
        if i == 0:
            a.append(num)
        else:
            b.append(num)
  

cnt = 0
flag = False
for x in range(n-2):
    for y in range(m-2):
        
        for l in range(x, x+3):
            for k in range(y, y+3):
                if a[l][k] == 0:
                    a[l][k] = 1
                else:
                    a[l][k] = 0
                cnt += 1
        
for l in range(n):
    for k in range(m):
        if a[l][k] != b[l][k]:
            flag = True
        
        
if flag:
    print(-1)
else:
    print(cnt)
    