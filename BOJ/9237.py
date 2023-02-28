# 이장님 초대

n = int(input())
t_list = list(map(int, input().split()))

t_list.sort(reverse=True)

growing_up = []
for i in range(1, len(t_list)+1):
    growing_up.append(i + t_list[i-1])
    
print(max(growing_up)+1)