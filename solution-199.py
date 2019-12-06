#DAILY CODING PROBLEM 199

def correct_braces(braces):
    braces_corrected=''
    corrections=0
    open_braces=0
    for brace in braces:
        if brace=='(':
            open_braces +=1
            braces_corrected +='('
        if brace==')':
            if (open_braces!=0):
                open_braces -=1
                braces_corrected +=')'
            else:
                corrections +=1

    braces_corrected +=')'*open_braces
    corrections +=open_braces
    return braces_corrected,corrections

assert correct_braces('()(()((')[0]=='()(()(()))'
assert correct_braces('()()))(())((((')[0]=='()()(())(((())))'
assert correct_braces(')(')[0]=='()'
assert correct_braces('"()())()')[0]=='()()()'
