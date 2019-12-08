def can_reach_end(jump): 
    how_far =[-1]*(len(jump))
    how_far[0]=0  
    for j in range(len(jump)):
        for i in range(j+1,len(jump)):
            if how_far[j]>-1 and j+jump[j]>=i:
                #not necessary but...
                how_far[i]=j if how_far[i]==-1 else min(how_far[i],j)
    return True if how_far[-1]>-1 else False

assert can_reach_end([2, 0, 1, 0])==True
assert can_reach_end([1, 1, 0, 1])==False
