#this one for testing -doing opposite -converts num to letter
def get_spreadshet_num(spreadsheet=''):
    spreadsheet_num=0
    multiplyby=ord('Z')-ord('A')+1
    for i,s in enumerate(spreadsheet[::-1]):
        spreadsheet_num +=(ord(s)-ord('A')+1)*pow(multiplyby,i)
    return spreadsheet_num

#this one -converts letter to num
def get_spreadshet_letter(to_code=0):
    base=64
    interval=ord('Z')-ord('A')+1
    coded=''

    while to_code>0:
        current_letter=to_code % interval
        to_code=to_code//interval
        if current_letter>0:
            coded=chr(current_letter+base)+coded  
        #handling somehow with last letter...
        else:
            coded='Z'+coded
            to_code -=1
    return coded

assert get_spreadshet_letter(1)=='A'
assert get_spreadshet_letter(27)=='AA'
assert get_spreadshet_letter(35881)=='BABA'
assert get_spreadshet_letter(475254)=='ZZZZ'
