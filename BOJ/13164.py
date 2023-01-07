# 행복 유치원
n, k = map(int, input().split())
s = list(map(int, input().split()))

# # 풀이 1번
# diff = []

# for i in range(1, len(s)):
#     diff.append(s[i] - s[i-1])
    
# diff.sort()
# count = 0

# for j in range(n-k):
#     count += diff[j]
    
# print(count)

# 풀이 2번

def solution():
    diff = []
    for i in range(len(s)-1):
        diff.append(s[i+1] - s[i])
        
    diff.sort(reverse=True)
    answer = sum(diff[k-1:])
    
    return answer

print(solution())