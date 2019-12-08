def Collatz_seq_check(num,n=1000000):
    tries=0
    num_=num
    while num>1:
        num = num/2 if num%2 ==0 else 3*num+1
        tries +=1
        if (tries>n)and(num>num_):
            raise Exception('Test failed after {} tries (Number: {}, Current: {})'.format(n,num_,int(num)))
    return tries
#The biggest output
number={'tries': 0, 'number': 0}
for i in range(800000,1000000):
    tries=Collatz_seq_check(i,380)
    if (number['tries']<tries):
        number['tries'], number['number']=tries,i
print("Input n <= 1000000 that gives the longest sequence is {} seq: {}"\
      .format(number['number'],number['tries']))
