# 완전제곱수
import math

m = int(input())
n = int(input())

list = []
for i in range(m, n+1):
    if math.sqrt(i) == int(math.sqrt(i)):
       list.append(i)
       
if len(list) == 0:
    print(-1)
    
else:
    print(sum(list))
    print(min(list))