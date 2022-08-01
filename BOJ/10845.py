# 큐 기본구조 (파이썬에선 리스트 형태)
from collections import deque
import sys
n = int(sys.stdin.readline())
queue = deque([])

for i in range(n):
    t = list(map(str, sys.stdin.readline().split()))
    if len(t) > 1:
        queue.append(int(t[1]))
    
    else: 
        if t[0] == 'pop':
            if len(queue) != 0:
                print(queue.popleft())
            else:
                print(-1)
                
        elif t[0] == 'size':
            print(len(queue))
            
        elif t[0] == 'empty':
            if len(queue) != 0:
                print(0)
            else:
                print(1)
                
        elif t[0] == 'front':
            if len(queue) != 0:
                print(queue[0])
            else:
                print(-1)
                
        elif t[0] == 'back':
            if len(queue) != 0:
                print(queue[-1])
            else:
                print(-1)
                
        

    
    