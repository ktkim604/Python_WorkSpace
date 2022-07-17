n = input().split('-')
num = []

for i in n:
    cnt = 0
    m = i.split('+')
    
    for j in m:
        cnt += int(j)
    num.append(cnt)
    
n1 = num[0]
for k in range(1, len(num)):
    n1 -= num[k]
    
print(n1)
    