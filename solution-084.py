atrix = [
    [1, 0, 0, 0, 0],
    [0, 0, 1, 1, 0],
    [0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [1, 1, 0, 0, 1],
    [1, 1, 0, 0, 1],
]
islands=[[0] * len(matrix[0]) for _ in range(len(matrix))]
def mark_island(i,j):
    #check_boundaries
    if ((i<0)or(j<0)or(i>=len(islands))or(j>=len(islands[0]))):
        return
    if (matrix[i][j]==1)and(islands[i][j]==0):
        islands[i][j]=1
        for x in range(-1,2):
            for y in range(-1,2):
                if not((x==0)and(y==0)):
                    mark_island(i+x,j+y)             
    else:
        return
    
def count_islands(matrix):
  
    count_islands=0
    for j in range(len(matrix)):
        for i in range(len(matrix[0])):
            if (matrix[j][i]==1)and(islands[j][i]==0):
                count_islands +=1
                mark_island(j,i)
    return count_islands

assert count_islands(matrix)==4
