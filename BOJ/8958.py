n = int(input())

for i in range(5):
    a = input()
    cnt = 0
    sum = 0
    total = 0
    for j in a:
        if j == "O":
            cnt += 1
            sum += cnt
            total += sum 
        elif j == "X":
            cnt += 0
            sum = 0
            total = 0
    print(total)