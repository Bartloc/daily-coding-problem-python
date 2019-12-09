def overlaping_inter(inter):
    def overlaps(a,b):
        return False if (a[1]<=b[0])or(b[1]<=a[0]) else True
    
    overlap=0
    x=1
    sort=sorted(inter,key=lambda inter: inter[1])
    for i in range(1,len(sort)):
        #overlaping
        if overlaps(sort[i-x],sort[i]):
            overlap +=1
            x +=1
        else:
            x=1
    return overlap
assert overlaping_inter(((7, 9), (2, 4), (5, 8)))==1
