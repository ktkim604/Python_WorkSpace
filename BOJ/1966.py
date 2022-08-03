import sys
n = int(input())

for i in range(3):
    m1, m2 = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))
    idx = [0 for i in range(m1)]
    idx[m2] = 1
    cnt = 0
    
    while True:
        if a[0] == max(a):
            cnt += 1
            if idx[0] != 1:
                del a[0]
                del idx[0]
            else:
                print(cnt)
                break
        else:
            a.append(a.pop(0))
            idx.append(idx.pop(0))


        
    