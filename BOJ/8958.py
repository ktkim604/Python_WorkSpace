n = int(input())

for i in range(n):
    a = input()
    cnt = 0
    sum = 0
    base = 1
    
    for j in a:
        if j == "O":
            sum = sum + base + cnt
            cnt += 1
            
        elif j == "X":
            cnt = 0
            
    print(sum)