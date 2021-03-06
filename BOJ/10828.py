# 스택 기본구조 (파이썬에선 리스트 형태)
import sys
n = int(sys.stdin.readline())
stack = []

for i in range(n):
    t = list(map(str, sys.stdin.readline().split()))
    if len(t) > 1:
        stack.append(int(t[1]))
    
    else: 
        if t[0] == 'pop':
            if len(stack) != 0:
                print(stack.pop())
            else:
                print(-1)
                
        elif t[0] == 'size':
            print(len(stack))
            
        elif t[0] == 'empty':
            if len(stack) != 0:
                print(0)
            else:
                print(1)
                
        else:
            if len(stack) != 0:
                print(stack[-1])
            else:
                print(-1)
                
        

    
    