from collections import deque

n, k = map(int, input().split())
circle = deque([])
for i in range(1, n+1):
    circle.append(i)

print('<', end = '')
while circle:
    for i in range(k-1):
        circle.rotate(-1)
    print(circle.popleft(), end='')
    
    if circle:
        print(', ',end='')
print('>')
