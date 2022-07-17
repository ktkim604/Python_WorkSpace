#주식

t = int(input())
for i in range(t):
    n = int(input())
    price = list(map(int, input().split()))
    
    result = 0
    max_price = 0
    
    for j in range(len(price)-1, -1, -1):
        if price[j] > max_price:
            max_price = price[j]
        else:
            result += max_price - price[j]
            
    print(result)       