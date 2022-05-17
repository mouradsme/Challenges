def Factors(x):
    result = []
    i = 1
    while i*i <= x:
        if x % i == 0:
            result.append(i)
            if x//i != i: 
                result.append(x//i)
        i += 1
    return result
    
def Palindrome(i):
    i = str(i)
    l = len(i)//2 
    return i[0:l]==i[l + (1 if len(i)%2==1 else 0):][::-1]

def Solution():
    T = int(input())
    for t in range(1, T+1):
        A = 0 
        TestCase = int(input())
        for n in Factors(TestCase):
            if (Palindrome(n)): A+=1
        print("Case #{}: {}".format(t, A))
Solution()