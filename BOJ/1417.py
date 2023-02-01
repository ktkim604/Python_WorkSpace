# 국회의원 선거

N = int(input())

people = []
for i in range(N):
    people.append(int(input()))
    
cnt = 0
dasom = people[0]
another = people[1:]


if N == 1:
    print(0)

else:
    another.sort(reverse=True)
    while True:
        if another[0] < dasom:
            break
        
        dasom += 1
        another[0] -= 1
        cnt += 1
        
        another.sort(reverse=True)
    
    print(cnt)
        
        