from collections import deque

n, k = map(int, input().split())

circle = deque([])

for i in range(1, n+1):
    circle.append(i)

print('<', end = '')
while circle:
    for i in range(k-1):
        circle.append(circle[0])
        circle.popleft()
    print(circle.popleft(), end='')
    
    if circle:
        print(', ',end='')
    
print('>')
