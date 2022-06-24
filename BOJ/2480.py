A, B, C = map(int, input().split())

if A==B==C:
    price = 10000 + A*1000
elif A==B or B==C or A==C:
    if A==B:
        price = 1000 + A*100
    elif B==C:
        price = 1000 + B*100
    else:
        price = 1000 + C*100
else:
    price = max(A,B,C)*100
    
print(price)