def nearest_sparse_number(number):
    
    pri_number=(str(bin(number))Problem 217
    out_number=pri_number[-1]
    number=number >>1
    
    while number>0:
        if (number%2)==0:
            out_number ='0'+out_number
        elif out_number[0]=='1':
            out_number ='0'*(len(out_number)+1)
            number+=1
        else:
            out_number ='1'+out_number
        number=number >>1
        
    return int(out_number,2)


assert (nearest_sparse_number(21))==21
assert (nearest_sparse_number(22))==32
