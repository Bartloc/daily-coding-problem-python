from collections import Counter

def rearrange(s):
    str1=str2=str3=''
    for c1,c2 in Counter(s).most_common():
        str2,str1 =(str2+c2*c1,str1)  if len(str1)+c2>len(str2) else (str2, str1+c2*c1) 
    str1,str2 = (str2,str1) if len(str2)>len(str1) else (str1,str2)

    if len(str1)-len(str2)>1:
        a=(len(str1)-len(str2))//2
        str2=str2+str1[:a]
        str1=str1[a:]

    if str1[-1]!=str2[-1]:
        for i,x in enumerate(str1):
            str3 +=str1[i]
            if i<len(str2):
                str3 +=str2[i]
        return str3
    else:
        return None

assert rearrange('aaabbc')=='babaca'
assert rearrange('aaab')==None
assert rearrange('aaabbbccc')=='ababcbcac'
