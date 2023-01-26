# 큐2
from collections import deque
import sys

n = int(input())
q = deque([])

for i in range(n):
    t = list(map(str, sys.stdin.readline().split()))
    
    if t[0] == 'push':
        q.append(int(t[1]))
        
    elif t[0] == 'pop':
        if len(q) != 0:
            print(q.popleft())
        else:
            print(-1)
    
    elif t[0] == 'size':
        print(len(q))
            
    elif t[0] == 'empty':
        if len(q) == 0:
            print(1)
        else:
            print(0)
    
    elif t[0] == 'front':
        if len(q) != 0:
            print(q[0])
        else:
            print(-1)
    
    elif t[0] == 'back':
        if len(q) != 0:
            print(q[-1])
        else:
            print(-1)
        