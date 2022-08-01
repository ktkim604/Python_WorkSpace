from collections import deque
import sys
n = int(sys.stdin.readline())
q = deque([])

for i in range(n):
    t = list(map(str, sys.stdin.readline().split()))
    
    if len(t) == 2:
        if t[0] == 'push_front':
            q.appendleft(t[1])
        elif t[0] == 'push_back':
            q.append(t[1])
            
    elif len(t) == 1:
        if t[0] == 'pop_front':
            if len(q) != 0:
                print(q.popleft())
            else:
                print(-1)
        elif t[0] == 'pop_back':
            if len(q) != 0:
                print(q.pop())
            else:
                print(-1)
        elif t[0] == 'size':
            print(len(q))
        elif t[0] == 'empty':
            if len(q) != 0:
                print(0)
            else:
                print(1)
                
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