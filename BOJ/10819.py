# 차이를 최대로
from itertools import permutations

n = int(input())
a = list(map(int, input().split()))

permu = list(permutations(a))

answer = 0
for p in permu:
    sum = 0
    for i in range(n-1):
        sum += abs(p[i] - p[i+1])
    
    if answer < sum:
        answer = sum
    
print(answer)
