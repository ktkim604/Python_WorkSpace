# 브루트 포스 (블랙잭)

n1, n2 = map(int, input().split())
m = list(map(int, input().split()))
result = 0

for i in range(n1):
    for j in range(i+1, n1):
        for k in range(j+1, n1):
            if m[i] + m[j] + m[k] > n2:
                continue
            else:
                result = max(result, m[i] + m[j] + m[k])
print(result)


