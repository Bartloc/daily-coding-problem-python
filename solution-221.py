def find_nth_number(i,num=7):
    if not isinstance(i,int) or i<0:
        raise Exception('i ={}: shall be int and >=0'.format(i))
    nth=0
    if i==0:
        nth=1
    elif i==1:
        nth=num
    elif i%2==1:
        nth=pow(num,i//2+1)
    elif i%2==0:
        for j in range(i//2+1):
            nth +=pow(num,j)
    else:
         raise Exception('for input {}: Unexpected error'.format(i))
    return nth

find_nth_number(2)
