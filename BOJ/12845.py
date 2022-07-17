n = int(input())
lev = list(map(int, input().split()))
lev.sort(reverse=True)

max_lev = lev[0]
gold = 0

for i in range(1, len(lev)):
    gold += (max_lev + lev[i])
    
print(gold)
