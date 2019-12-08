import random
#converts rand_x to rand_y
def rand_x_to_y(x=1,y=1):
    out=0
    for _ in range(y):
        out += random.randint(1,x)      
    return out%y+1
    

#testing

rand_in=5
rand_out=10
margin=0.10
x=10000
d={i+1:0 for i in range(rand_out)}

for _ in range(x):
    d[rand_x_to_y(rand_in,rand_out)] +=1

expected_value=x//rand_out
for d_key,d_val in d.items():
    diff=abs((d_val-expected_value)/expected_value)
    if diff>margin:
        raise Exception('rand_x_y Error - margin exceeded')
