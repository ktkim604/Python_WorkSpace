from collections import deque

n = int(input())
dq = deque()

for i in range(1, n+1):
    dq.append(i)
     
while len(dq) != 1:
    dq.popleft()
    dq.rotate(-1)
    
    
print(dq[0])
        