rect=({
    "top_left": (1, 4),
    "dimensions": (3, 3) # width, height
},
{
    "top_left": (-1, 3),
    "dimensions": (2, 1)
},
{
    "top_left": (0, 5),
    "dimensions": (4, 3)
})

def check_rect(rect):
    def check_if_inside(q1,p1,q2,p2):
        return True if (q1<=p1 and q2>=p2)or(p1<=q1 and p2>=q2) else False
    
    for i in range(len(rect)):
        for x in range(i):
            if check_if_inside(rect[i]['top_left'][0],rect[x]['top_left'][0], \
                               rect[i]['dimensions'][0],rect[x]['dimensions'][0]) \
            and \
            check_if_inside(rect[i]['top_left'][1],rect[x]['top_left'][1],\
                            rect[i]['dimensions'][1],rect[x]['dimensions'][1]):
                return True
    return False
    
assert check_rect(rect)==True
