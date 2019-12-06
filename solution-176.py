def mapping(s1,s2):
    dx={}
    if not len(s1)==len(s2):
        return False
    for ch1,ch2 in zip(s1,s2):
        if not ch1 in dx:
            if ch2 in dx.values():
                return False
            dx[ch1]=ch2
        elif dx[ch1]!=ch2:
            return False
    return True

assert mapping('abc','bcd')==True
assert mapping('foo','bar')==False
