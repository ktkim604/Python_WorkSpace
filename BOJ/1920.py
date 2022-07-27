# 이분 탐색
import sys

n = int(sys.stdin.readline())
n1 = list(map(int, sys.stdin.readline().split()))
n1.sort()

m = int(sys.stdin.readline())
m1 = list(map(int, sys.stdin.readline().split()))

def binary_search(target, data):
    start = 0
    end = len(data) - 1
    
    while start <= end:
        mid = (start + end) // 2
        
        if data[mid] == target:
            return 1
        elif data[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return 0
    

for i in m1:
    print(binary_search(i, n1))
    

