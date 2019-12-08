def maxPaths(mat_size=(0,0)):
    if not mat_size[0]:
        return 0
    DP=[[0]*mat_size[0] for x in range(mat_size[1])]
    DP[0][0]=1
    for i in range(mat_size[0]):
        for j in range(mat_size[1]):
            DP[j][i]=DP[j-1][i]+DP[j][i-1] if (j!=0)and(i!=0) else 1
    return(DP[-1][-1])
assert maxPaths((5,5))==70
