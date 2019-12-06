def longest_1_in_bin(num=0):
    l=0
    max_l=0
    for a in str(bin(num))[2:]:
        if int(a)==0:
            max_l=max(max_l,l)
            l=0
        else:
            l +=1  
    return max_l
assert longest_1_in_bin(156)==3
