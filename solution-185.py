#Works for all dimensions (2D,4D, 5D etc) - just add next value to tuples top_left and dimensions
q={
    "top_left": (1, 4,1),
    "dimensions": (3,3,1) # width, height
}
p={
    "top_left": (0,5,1),
    "dimensions": (4,3,1) # width, height
}
def check_distance(q1,p1,q2,p2):
    x1=p1 if p1>q1 else q1
    x2=p2 if p2<q2 else q2
    return x2-x1
rec=1    
for x,y in enumerate(q["top_left"]):    
    rec *=check_distance(q["top_left"][x],p["top_left"][x],\
                         q["top_left"][x]+q["dimensions"][x],p["top_left"][x]+p["dimensions"][x])
rec=rec if rec>0 else 0
print(rec)
