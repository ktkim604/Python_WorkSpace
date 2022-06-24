H, M = map(int, input().split())

if M<45:
    if(H == 0):
        H = 24
    H -= 1
    M = 60 - (45-M)
    print(H, M)
    
else:
    M = M-45
    print(H, M)