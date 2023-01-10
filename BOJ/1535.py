# 안녕
import itertools

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

new_list = []

for i , j in zip(a,b):
    temp = str(i) + ',' +str(j)
    new_list.append(temp)

s = []

for i in range(1, n+1):  
    permu_list = list(itertools.combinations(new_list,i))
    for permu in permu_list:
        
        temp_list = [int(i.split(',')[0]) for i in permu]
        
        if sum(temp_list)< 100:
            s.append(permu)
            
answer = 0

for temp_list in s:
    S = 0 
    for i in temp_list:
        S += int(i.split(',')[1])
        
    answer = max(answer,S)
    
print(answer)