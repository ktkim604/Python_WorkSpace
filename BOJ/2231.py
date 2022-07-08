n = int(input())
s = 0
arr = []
for i in range(n+1):
    a = list(map(int, str(i)))
    s = i
    s = s + sum(a)
    
    
    if s== n:
        arr.append(i)

print(min(arr))
    
        
