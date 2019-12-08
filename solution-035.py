def RGB_sort(base):
    j = 0
    for i in range(len(base)):
        if (base[i] == 'R'):
            base.insert(0, base.pop(i))
            j += 1
        elif (base[i] == 'G'):
            base.insert(j, base.pop(i))

    return base

#testing
from random import shuffle
for i in range(100):
    base=['G', 'B', 'R', 'R', 'B', 'R', 'G']
    shuffle(base)
    assert RGB_sort(base)== ['R', 'R', 'R', 'G', 'G', 'B', 'B']
