# 막대기
import sys

start = 64
stick = []
stick.append(start)
X = int(input())

while True:
    stick.append(start//2)
    start = start - (start//2)
    
    if start == 1:
        break
    
cnt = 0
for i in range(len(stick)):
    if X >= stick[i]:
        X -= stick[i]
        cnt += 1
        
    if X == 0:
        break
    
print(cnt)