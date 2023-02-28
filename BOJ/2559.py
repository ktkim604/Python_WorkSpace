N, K = map(int, input().split())
arr = list(map(int, input().split()))

ans = []
ans.append(sum(arr[:K]))

for i in range(N-K):
    ans.append(ans[i] - arr[i] + arr[K+i])

print(max(ans))
