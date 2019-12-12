def product(ini):
    prod=[]
    for i in range (pow(2,len(ini))):
        subprod={x[0]*int(x[1]) for x in (zip(ini,bin(i)[2:][::-1])) if int(x[1])>0}
        prod.append(subprod)
    return prod

assert product([1,2,3])==[set(), {1}, {2}, {1, 2}, {3}, {1, 3}, {2, 3}, {1, 2, 3}]
assert product([])==[set()]
