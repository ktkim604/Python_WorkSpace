n = int(input())

roads = list(map(int, input().split()))
cities = list(map(int, input().split()))

min_cost = cities[0]

sum = 0
for i in range(n-1):
    if min_cost > cities[i]:
        min_cost = cities[i]
    sum += min_cost * roads[i]
    
print(sum)