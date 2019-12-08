def findMin(i,subset1=(),subset2=()):
       
    if i==0:
        return abs(sum(subset1)-sum(subset2)),subset1,subset2
    return min(findMin(i-1,subset1+(subset2[i-1],),subset2[0:i-1]+subset2[i:]),\
               (findMin(i-1,subset1,subset2)))
    
arr=[5, 10, 15, 20, 25]
diff,subset1,subset2=findMin(len(arr),subset2=tuple(arr)) 
assert (subset1,subset2)==((20,10,5),(15,25))
