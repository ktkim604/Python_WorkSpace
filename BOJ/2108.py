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
    mid_num = (len(data) // 2) + 1
    return mid_num

def frequency(data):
    frequency_num = Counter(num)
    return frequency_num(1)[0][0]

def size(data):
    size_num = num[-1] - num[0]
    return size_num

print(avg(num))
print(mid(num))
print(frequency(num))
print(size(num))
    



