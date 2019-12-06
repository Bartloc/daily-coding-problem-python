def reorder(nset,perm):
    return [x[1] for x in (sorted(zip(perm,nset)))]

reorder(nset,perm)
assert reorder(["a", "b", "c"],[2, 1, 0])==["c", "b", "a"]
assert reorder(['a', 'b', 'c', 'd'],[3, 0, 1, 2])==['b', 'c', 'd', 'a']
