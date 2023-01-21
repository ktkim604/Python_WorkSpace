import sys

n, m = map(int, input().split())

n_lst = []
for i in range(n):
    n_lst.append(input())
    
m_lst = []
for j in range(m):
    m_lst.append(input())
    
cnt = 0
for M in m_lst:
    if M in n_lst:
        cnt += 1
print(cnt)