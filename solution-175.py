l=[
  ('a', 'a', 0.9),
  ('a', 'b', 0.075),
  ('a', 'c', 0.025),
  ('b', 'a', 0.15),
  ('b', 'b', 0.8),
  ('b', 'c', 0.05),
  ('c', 'a', 0.25),
  ('c', 'b', 0.25),
  ('c', 'c', 0.5)
]
from random import random

def Markow_tran_prob(l,n=5000):
    curr_state='a'
    counter={'a':0, 'b':0 ,'c':0}
    counter[curr_state] +=1
    for _ in range(0,n):
        jump=random()
        for x in l:
            if (x[0]==curr_state):
                if (jump<=x[2]):
                    curr_state=x[1]
                    counter[x[1]] +=1
                    break
                else:
                    jump=jump-x[2]
    return counter
print(Markow_tran_prob(l))
