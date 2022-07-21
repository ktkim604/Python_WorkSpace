k, n = map(int, input().split())

len_list = []
for i in range(k):
    length = int(input())
    len_list.append(length)
    
answer = 0    
    
start = 1
end = max(len_list)

while (start <= end):
    mid = (start + end) // 2
    cnt = 0
    for j in range(k):
        cnt += len_list[j] // mid

    print(cnt,start,end,mid)
    # if cnt == n:
    #     answer = max(answer,mid)
    if cnt >= n:
        start = mid + 1
    else:
        end = mid - 1
        
print(start)    