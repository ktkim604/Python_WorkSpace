# 이진탐색

n = int(input())
n1 = list(map(int, input().split()))

m = int(input())
m1 = list(map(int, input().split()))

n1.sort()

cnt = {}
for card in n1:
    if card in cnt:
        cnt[card] += 1
    else:
        cnt[card] = 1

def search_binary(target, data, start, end):
    
    if start > end:
        return 0
    
    mid = (start + end) // 2
    
    if data[mid] == target:
        return cnt.get(target)
    elif data[mid] < target:
        return search_binary(target, data, mid+1, end)
    else:
        return search_binary(target, data, start, mid-1)
        
for target in m1:
    print(search_binary(target, n1, 0, len(n1)-1), end=' ')
        