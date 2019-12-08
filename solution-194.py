list2=[6, 4, 5, 1]
list1=[1, 4, 5, 6]

def inter_pairs(list1=[],list2=[]):
    intersec=0
    for i, (segm_a1,segm_a2) in enumerate(zip(list1,list2)):
        for  _,(segm_b1,segm_b2) in enumerate(list(zip(list1,list2))[i+1:]):
            if ((segm_a1)<(segm_b1)and(segm_a2)>(segm_b2))or\
                ((segm_b1)<(segm_a1)and(segm_b2)>(segm_a2)):
                    intersec +=1
    return intersec
    
assert inter_pairs(list1,list2)==5
