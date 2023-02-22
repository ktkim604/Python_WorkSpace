# 토너먼트
import sys
input = sys.stdin.readline

N, kim, im = map(int, input().split())

cnt = 0
while True:
    if kim == im:
        break
    
    kim -= kim // 2
    im -= im // 2
    cnt += 1

print(cnt)