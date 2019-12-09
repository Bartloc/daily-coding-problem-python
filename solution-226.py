def find_dict(words):
    alphabet=''
    #add first letter to dictionary 
    for i in range(len(words)):
        if words[i][0] not in alphabet:
            alphabet +=words[i][0] 

    i=0
    for k,word_prev in enumerate(words):
        ex=0
        for l,word_next in enumerate(words[k+1:]):
            if ex==1:
                    break
            for i in range(len(word_prev)):
                
                if (i+1)<len(word_prev) and (i+1)<len(word_next)\
                and word_prev[:i]==word_next[:i]:
                    if word_prev[i+1] in alphabet and word_next[i+1] in alphabet\
                    and word_prev[i+1]!=word_next[i+1]:
                        ex=1
                        break
                    if word_prev[i+1] not in alphabet and word_next[i+1] in alphabet:

                        for m in range(len(alphabet)):
                            if word_next[i+1]==alphabet[m]:
                                alphabet = alphabet[:m]+word_prev[i+1]+alphabet[m:]
                                ex=1
                                break
                    
                    if word_next[i+1] not in alphabet and word_prev[i+1] in alphabet:

                        for m in range(len(alphabet)):
                            if word_prev[i+1]==alphabet[m]:
                                alphabet = alphabet[:m+1]+word_next[i+1]+alphabet[m+1:]
                                ex=1
                                break
                   
    return list(alphabet)


assert find_dict(['xww', 'wxyz', 'wxyw', 'ywx', 'ywz'])==['x', 'z', 'w', 'y']
assert find_dict(["caa", "aaa","aam", "aab"])==['c', 'a', 'm', 'b']
assert find_dict(["baa", "abcd", "abca", "cab", "cad","cam"])==['b', 'd','m', 'a', 'c']
