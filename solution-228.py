def largest_pos_int(t):
    out={x:0 for x in t}
    for i in range(len(t)):
        for j in range(i+1,len(t)):
            if int((str(t[i]))+str(t[j]))>int((str(t[j]))+str(t[i])):
                    out[t[i]] +=1

            else:
                    out[t[j]] +=1
    return int(('').join(list(map(lambda x: str(x),sorted(out,key=lambda x: out[x],reverse=True)))))

assert largest_pos_int([10, 7, 76, 415])==77641510
assert largest_pos_int([54, 546, 548, 60 ,901,9,97])==9979016054854654
