def find_set(set1):
    set_cand=[tuple()]* len(set1)
    for j in range(len(set1)):
        for x in range(j):
            if (set1[j]%set1[x])==0 or (set1[x]%set1[j])==0:
                set_cand[j] +=set1[x],
        set_cand[j] +=set1[j],
    
    return list(max(set_cand,key=lambda x: len(x)))


assert find_set([3, 5, 10, 20, 21])==[5,10,20]
assert find_set([1,3,6, 24])==[1,3,6,24]
