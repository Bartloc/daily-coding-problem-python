#Permutation
def newPerm(perm):
    perm=str(perm)
    newperm=''
    breakpoint=0
    
    for i in range(len(perm)-2,-1,-1):
        if perm[i]<perm[i+1]:
            newperm=perm[0:i]
            breakpoint=i
            break
    else:
        return False
    
    for i in range(breakpoint+1,len(perm)):

        if perm[i]>perm[breakpoint]:
            breakpoint_2=i
            cand=perm[i]
    
    rest=('').join(sorted(perm[breakpoint:breakpoint_2]+perm[breakpoint_2+1:]))
    
    newperm=newperm+cand+rest
    
    return int(newperm)

assert newPerm(48975)==49578
