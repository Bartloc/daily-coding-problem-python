arr=['a', 'b', 'c']
perm=[3, 0, 1, 2]

apply_arr_to_perm=lambda arr,perm:[x[1] for x in (sorted(zip(perm,arr)))]

assert apply_arr_to_perm(['a','b','c'],[2,1,0])==['c','b','a']
