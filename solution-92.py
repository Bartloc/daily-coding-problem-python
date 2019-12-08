csc={'CSC300': ['CSC100', 'CSC200'], 'CSC200': ['CSC100'], 'CSC100': []}
temp_csc=csc.copy()
courses=[]
def find_csc(csc):
    if not csc:
        return courses
    for (key,value) in csc.items():
        if value==courses:
            courses.append(key)
            del csc[key]
            return find_csc(csc)
    return False


assert find_csc(temp_csc)== ['CSC100', 'CSC200', 'CSC300'] 
