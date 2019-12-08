def distinct(arr):
    dist=[0]*len(arr)
    for i in range (len(arr)):
        can=len(arr)
        for x in range(i):
            if arr[x]==arr[i]:
                    can=i-x   
        dist[i]=min(dist[i-1]+1,can) if i>0 else 1
    return max(dist)
assert distinct([5, 1, 3, 5, 2, 3, 4, 1])==5
