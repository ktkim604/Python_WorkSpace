n = int(input())
cnt = n

for i in range(n):
    t = input()
    for j in range(len(t)-1):
        if t[j] == t[j+1]:
            pass
        elif t[j] in t[j+1:]:
            cnt -= 1
            break
print(cnt)