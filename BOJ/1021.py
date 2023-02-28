# 회전하는 큐

from collections import deque

N, M = map(int, input().split())
num = list(map(int, input().split()))

q = deque()
for i in range(1, N+1):
    q.append(i)
    

cnt = 0

for j in num:
    while True:
       
       if q[0] == j:
           q.popleft()
           break
       
       else:
           if q.index(j) <= len(q) // 2:
               q.rotate(-1)
               cnt += 1
               
           else:
               q.rotate(1)
               cnt += 1
               
print(cnt)