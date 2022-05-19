Print = True
def Portions(List):
    Portions = []
    last = List[0]
    Portion = [last]
    Details = []
    for i in range(1, len(List)):
        x = List[i]
        if (x != last ):
            Portions.append(Portion)
            Portion = [x]
            Details.append(last)
        else:
            Portion.append(x)
        last = x
    Details.append(last)
    Portions.append(Portion) 
    return [Portions, Details]
def Normalize(List):
    L = []
    for x in List:
        for i in x:
            L.append(i)
    return L
    
def solve(List, I, Max):
    L = List[1]
    if (len(L)-1<=I):I=len(L)-1
    i = I # - len(List[0][I]) + 1
    Left = L[i-1] if i-1 >= 0 else float('inf')
    Right =  L[i+1] if i+2 <= len(L) else float('inf')

    target = List[1][I]
    if (Left == Right == float('inf')):
        target = 0
        Rotated = abs(L[0])
    else:
        if (Left < Right):
            target = Left 
        if (Right < Left):
            target = Right
        if (Left == Right):
            target = Left
        if (L[I] > target):
            goingUp = Max  - L[I] + target + 1  # rotate up
            goingDown = L[I] - target # rotate down
        if (L[I] <= target):
            goingDown = L[I] + Max  - target + 1  # rotate up
            goingUp = target - L[I] # rotate down

        if( goingUp <= goingDown ):
            Rotated = abs(goingUp)
            if Print: print("Up ", List[1][I], " == > ", target, goingUp, " Rotated ", Rotated)
        else:
            Rotated = abs(List[1][I]-goingDown)
            if Print: print("Down ", List[1][I], " == > ", target, goingDown, " Rotated ", Rotated)
    List[1][I] = target
    List[0][I] = list(map(lambda x: target, List[0][I]))
    
    return (List, I, Rotated)

def Solution():
    Answers = ""
    T = int(input())
    for t in range(1, T+1):
        N, D = [int(i) for i in input().split()]
        Padlock = [int(i) for i in input().split()]
        Minimum = float('inf')
        for j in range(N):
            if Print: print("Case ", t, " Iter: ", j)
            Start = j 
            PadlockCopy = Padlock.copy()
            Sum = sum(PadlockCopy)
            c = 0
            while(Sum > 0):
                PortionsList = Portions(PadlockCopy)
                Result = solve(PortionsList, Start, D - 1)
                PadlockCopy = Normalize(Result[0][0])
                c+=Result[2]  
                Sum = sum(Result[0][1]) 
                Start = Result[1]
                
                if Print: 
                    print(Result[0][0])
                    print()
                
            
            if (c < Minimum): Minimum = c
            
            if Print: 
                print("Rotations = ", c)

                
        Answers = Answers + "Case #{}: {}".format(t, Minimum) + "\n"
    print(Answers)
        
Solution()