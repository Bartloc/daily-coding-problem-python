def trapped_water(walls):
    filled = 0
    left = walls[0]
    for w in walls:
        if w > left:
            left = w
        else:
            filled += left-w

    i = 0
    right = walls[-1]
    for l in walls[::-1]:
        if l > right:
            filled -= i*(l-right)
            right = l
        i = i+1
        
    return filled

assert trapped_water([2, 1, 2])==1
assert trapped_water([3, 0, 1, 3, 0, 5])==8
assert trapped_water([2000, 1, 10, 0, 100, 1, 1])==289
