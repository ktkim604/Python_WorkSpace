import sys

n, m  = map(int, sys.stdin.readline().split())
tree_length = list(map(int, sys.stdin.readline().split()))

start = 1
end = max(tree_length)

while (start <= end):
    mid = (start + end) // 2
    cnt = 0
    for i in range(n):
        if tree_length[i] >= mid:
            cnt += (tree_length[i] - mid)
            
    if cnt >= m:
        start = mid + 1
    else:
        end = mid - 1
    print(mid, cnt, start, end)
print(end)