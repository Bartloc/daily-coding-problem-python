def count_attacking_bish(bishpos=[(0,0)]):
    count_bish=0
    for i, (col_a,row_a) in enumerate(bishpos):
        for x, (col_b,row_b) in enumerate(bishpos[i+1:]):
            if  (col_a+row_a==col_b+row_b)or\
                (col_a-row_a==col_b-row_b):
                    count_bish +=1
    return count_bish
assert count_attacking_bish([(0, 0),(1, 2),(2,2),(4,0)])==2
assert count_attacking_bish([(0, 0), (1, 2), (2, 2)]) == 1
assert count_attacking_bish([ (2, 2), (3, 3),(0,4),(4,0)])==4
