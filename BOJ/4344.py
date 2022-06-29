
C = int(input())
for i in range(C):
    scores = list(map(int, input().split()))
    avg = sum(scores[1:])/scores[0]
    cnt = 0
    for j in scores[1:]:
        if avg < j:
            cnt += 1
    percent = (cnt/scores[0])*100
    print('%.3f' %percent + '%')