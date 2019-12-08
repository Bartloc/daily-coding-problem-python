def find_max_3prod(pro):
    if len(pro)<3:
        return False
    srt=sorted(pro)
    return max(srt[-1]*srt[-2]*srt[-3],srt[-1]*srt[0]*srt[1])  

assert find_max_3prod([-10,-10,5,2])==500
assert find_max_3prod([1, 10, 5, 2,100,2,1,30,23,-2,-300])==69000
