def find_pattern_pos(s,pattern):
    pattern_loc=[]
    for i in range(len(s)):
        if s[i:i+len(pattern)]==pattern:
            pattern_loc.append(i)
    return pattern_loc

assert find_pattern_pos('abracadabra','abr')==[0,7]
