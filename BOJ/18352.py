from collections import deque
import sys

def bfs(node):
    q = deque()
    q.append((node))
    
    while q:
        