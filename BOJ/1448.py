# 삼각형 만들기
import itertools
import sys
input = sys.stdin.readline

N = int(input())

num = [int(input()) for _ in range(N)]
num.sort(reverse=True)

for i in range(N-2):
    if num[i+1] + num[i+2] > num[i]:
        print(num[i] + num[i+1] + num[i+2])
        quit()
        
print(-1)
