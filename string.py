from math import isqrt
def solve(s):
    n = isqrt(len(s))
    if n*n!=len(s):
        return 0
    grid=[]
    ind=0
    for i in range(n):
        row=[]
        for j in range(n):
            row.append(s[ind])
            ind+=1
        grid.append(row)
        ans=0
    for i in range(n):
        flag=True
        for j in range(n-1):
            if (grid[i][j]!=grid[i][j+1]):
                flag=False
                break
        if(flag):
            ans+=1
    for i in range(n):
        flag=True
        for j in range(n-1):
            if (grid[j][i]!=grid[j+1][i]):
                flag=False
                break
        if(flag):
            ans+=1
    return ans

s=input()
print(solve(s))

