matrix=[[0,3,1,1],
       [2,0,0,4],
       [1,5,3,1]]

def collectMoney(matrix):
    mat_size=[0,0]
    mat_size[1]=len(matrix)
    mat_size[0]=len(matrix[0])
    DP=[[0]*mat_size[0] for x in range(mat_size[1])]
    for i in range(mat_size[0]):
        for j in range(mat_size[1]):
            DP[j][i]=matrix[j][i]+max(DP[j-1][i],DP[j][i-1]) 
    return(DP[-1][-1])

assert collectMoney(matrix)==12
