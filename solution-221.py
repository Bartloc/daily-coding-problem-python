nish =lambda n,num=7: sum(pow(num,i) for (i,x) in enumerate(bin(n)[2:][::-1]) if int(x)==1)\
      if n>0 else 0


#testing 
assert nish(5)==50
