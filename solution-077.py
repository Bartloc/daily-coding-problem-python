def merge_intervals(inter):
    sort=sorted(inter,key=lambda inter: inter[1])
    def merging(a,b):
        return (min(a[0],b[0]),max(a[1],b[1]))
    def overlaps(a,b):
        return False if (a[1]<=b[0])or(b[1]<=a[0]) else True
   
    merged=[inter[0]]
    
    for i in range(1,len(sort)):
        #merging
        if overlaps(merged[-1],sort[i]):
            merged[-1]=merging(merged[-1],sort[i])
            while (len(merged)>=2)and(overlaps(merged[-1],merged[-2])):
                    merged[-2]=merging(merged[-1],merged[-2])
                    merged.pop()
        else:
            merged.append(sort[i])
    return merged

assert merge_intervals(((1, 3), (5, 8), (4, 10), (20, 25)))==[(1, 3), (4, 10), (20, 25)]
