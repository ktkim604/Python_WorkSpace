A, B, V = map(int, input().split())

day = 0
height = 0

while True:
    day += 1
    height += A
    if height >= V:
        break
    height -= B

    
print(day)
    
    
    
