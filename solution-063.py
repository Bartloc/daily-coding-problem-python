def find_word(lrtb,word):
    for j in range(len(lrtb)):
        for i in range(len(lrtb[0])):
            if (word[0]==lrtb[j][i]):
                #check horizontal
                if not (len(word)+i)>len(lrtb[0]):
                    if word==(('').join(lrtb[j][i:i+len(word)])):
                        return True
                #check vertical
                if not (len(word)+j)>len(lrtb):
                    vertical=''
                    for x in range(len(word)):
                        vertical +=lrtb[j+x][i]
                    if word==vertical:
                        return True            
    return False

lrtb=[
    ['F', 'A', 'C', 'I'],
    ['O', 'B', 'Q', 'P'],
    ['A', 'N', 'O', 'B'],
    ['M', 'A', 'S', 'S']
    ]

assert find_word(lrtb,'FOAM')==True
assert find_word(lrtb,'MASS')==True
assert find_word(lrtb,'ABNB')==False
