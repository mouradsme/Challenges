import math
def Solution():
    T = int(input())
    for i in range(1, T+1):
        R, A, B = [int(i) for i in input().split()]
        Area = R**2;
        alternate = True
        while (R > 0):
            R = R * A if alternate else R//B  ;
            Area += R**2;
            alternate = not alternate
        print("Case #{}: {}".format(i, Area*math.pi));
Solution()