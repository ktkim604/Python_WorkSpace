from collections import deque
import sys

def bfs(node):
    q = deque()
    q.append((node))
    
    while q:
        
        
        
n, m, k, x = map(int, input().split())

for i in range(m):
    a, b = map(int, input().split())