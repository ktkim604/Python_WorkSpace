# 한 줄로 서기
import sys
input = sys.stdin.readline

N = int(input())

check = list(map(int, input().split()))
ans = [0] * N

for p in range(1, N+1):
    t = check[p-1]
    cnt = 0
    
    for i in range(N):
        if ans[i] == 0 and cnt == t:
            ans[i] = p
            break
            
        elif ans[i] == 0:
            cnt += 1
            
print(*ans)