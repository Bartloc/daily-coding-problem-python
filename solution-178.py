import random
def roll_dices(succ,pred,n=1000):
    succ_tries=0
    for _ in range(n):
        roll=True
        number_before=0
        tries=0
        #print(" ",end="\n")
        while roll:
            tries +=1
            number=random.randint(1,6)
            #print(number,end=',')
            if ((number==succ) and (number_before==pred)):
                succ_tries +=tries
                roll=False
            number_before=number
    return succ_tries/n

res56=roll_dices(5,6)
res55=roll_dices(5,5)

print('Choose 56 seq') if (res56<res55) else print('Choose 55 seq')
print('5 and 6 = {}, 5 and 5 = {}'.format(res56,res55))
