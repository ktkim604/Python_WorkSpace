n = int(input())

cnt = 0

while n >= 0:
    if n % 5 == 0:
        cnt += n // 5
        n -= n
        if n == 0:
            break
    n -= 3
    cnt += 1
if n < 0:
    print(-1)
else:
    print(cnt)
    
