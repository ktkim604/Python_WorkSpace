# 예산
import sys

def bin(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        
        target = 0
        for i in array:
            target += min(mid, i)
            
        if target > m:
            end = mid - 1 
        else:
            start = mid + 1
            
    return end
        

n = int(input())
per = list(map(int, input().split()))
m = int(input())



if sum(per) <= m:
    print(max(per))
    
else:
    ans = bin(per, 0, 0, max(per))
    print(ans)