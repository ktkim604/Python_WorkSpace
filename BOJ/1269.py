# 대칭 차집합
import sys
input = sys.stdin.readline

A, B = map(int, input().split())

A = set(map(int, input().split()))
B = set(map(int ,input().split()))

A_B = [i for i in A if i not in B]
B_A = [j for j in B if j not in A]
        
print(len(A_B) + len(B_A))

