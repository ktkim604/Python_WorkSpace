import sys
import math
from collections import Counter

n = int(input())
num = []
for i in range(n):
    num.append(int(sys.stdin.readline()))
num.sort()

def avg(data):
    avg_num = sum(data) / len(data)
    return round(avg_num)

def mid(data):
    mid_num = (len(data) // 2)
    return num[mid_num]

def frequency(data):
    cnt = Counter(data).most_common(2)
    if len(data) > 1:
        if cnt[0][1] == cnt[1][1]:
            return cnt[1][0]
        else:
            return cnt[0][0]
    else:
        return cnt[0][0]

def size(data):
    size_num = num[-1] - num[0]
    return size_num

print(avg(num))
print(mid(num))
print(frequency(num))
print(size(num))
