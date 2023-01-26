# 연구소
import sys
from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

visited = [[0]*m for j in range(n)]

print(visited)