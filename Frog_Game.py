def canAliceWin(n, a, b):
    L=0
    for i in range(t):
        if (a-b)%2==0:
            L=0
        else:
            L=1
            break
    if L==0:
        return("YES")
    else:
        return("NO")
