import sys

n = int(input())

s = []
for i in range(n):
    m = int(sys.stdin.readline())
    s.append(m)
    
s.sort()

for j in s:
    print(j)