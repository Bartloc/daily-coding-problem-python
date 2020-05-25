def enc(stri):
    if not stri:
        return None
    temp = stri[0]
    outstri = ''
    enc = 0
    for s in stri:
        if s == temp:
            enc = enc+1
        else:
            outstri = outstri + str(enc)+temp
            temp = s
            enc = 1
    outstri = outstri + str(enc)+temp
    return(outstri)


def dec(stri):
    outstri = ''
    numb = ''
    s = 0
    if not stri:
        return None
    for s in stri:
        num = s
        if num.isdigit():
            numb = numb+num
        else:
            temp = s * int(numb)
            outstri = outstri + temp
            numb = ''

    return outstri


assert enc('AAAABBBCCDAA') == '4A3B2C1D2A'
assert dec('4A3B2C1D2A') == 'AAAABBBCCDAA'
