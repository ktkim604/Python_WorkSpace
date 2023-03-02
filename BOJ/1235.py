# 학생 번호
import sys
input = sys.stdin.readline

N = int(input())

num_list = [input().rstrip() for _ in range(N)]

k = 1
while True:
    check = set()
    for num in num_list:
        check.add(num[-k:])
        
    if len(check) == N:
        break
    
    k += 1
    
print(k)
