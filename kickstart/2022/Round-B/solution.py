import math
T = int(input())
for i in range(1, T+1):
    R, A, B = [int(i) for i in input().split()]
    Area = R**2;
    while (R > 0):
        R = R * A  ;
        Area += R**2;
        R =R // B;
        Area += R**2;
    
    Area = Area * math.pi;            
    print("Case #{}: {}".format(i,Area));

