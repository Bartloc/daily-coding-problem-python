def sort_path(path):
    s_path=[]
    a_path=path.split('/')   
    for a in a_path:
        if a=='.':
            continue
        if a=='..':
            s_path.pop()
            continue
        s_path.append(a)
    return ('/').join(s_path)
    
assert sort_path('/usr/bin/../bin/./scripts/../')=='/usr/bin/'
